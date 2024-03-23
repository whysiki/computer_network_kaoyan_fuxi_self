# from multiprocessing import context
# from email.policy import HTTP
# from re import template
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Question, Choice, SubmittedIP
from django.template import loader
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# An object capable of resolving references to existing query objects
# Create your views here.


# def index(request) -> HttpResponse:
#     latest_question_list = Question.objects.order_by("-pub_date")[
#         :5
#     ]  # BaseManager[Question]
#     template = loader.get_template("polls/index.html")

#     context = {"latest_question_list": latest_question_list}

#     return HttpResponse(template.render(context, request))


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)

#     # 注意到，我们不再需要导入 loader 和 HttpResponse 。不过如果你还有其他函数（比如说 detail, results, 和 vote ）需要用到它的话，就需要保持 HttpResponse 的导入。
#     # render()函数的第一个参数是请求对象，第二个参数是模板名，第三个参数是可选的字典。它返回使用给定上下文呈现的给定模板的HttpResponse对象。


# # def detail(request, question_id) -> HttpResponse:
# #     # return HttpResponse("You're looking at question %s." % question_id)


# #     try:
# #         question = Question.objects.get(pk=question_id)
# #     except Question.DoesNotExist:
# #         raise Http404("Question does not exist")
# #     return render(
# #         request=request,
# #         template_name="polls/detail.html",
# #         context={"question": question},
# #     )


# # 尝试用 get() 函数获取一个对象，如果不存在就抛出 Http404 错误也是一个普遍的流程。Django 也提供了一个快捷函数，下面是修改后的详情 detail() 视图代码：
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

#     # get_object_or_404()函数接受一个Django模型作为它的第一个参数和任意数量的关键字参数，并将这些参数传递给模型管理器的get()函数。如果对象不存在，它会引发Http404。
#     设计哲学

#     # 为什么我们使用辅助函数 get_object_or_404() 而不是自己捕获 ObjectDoesNotExist 异常呢？还有，为什么模型 API 不直接抛出 ObjectDoesNotExist 而是抛出 Http404 呢？

#     # 因为这样做会增加模型层和视图层的耦合性。指导 Django 设计的最重要的思想之一就是要保证松散耦合。一些受控的耦合将会被包含在 django.shortcuts 模块中。

#     # 也有 get_list_or_404() 函数，工作原理和 get_object_or_404() 一样，除了 get() 函数被换成了 filter() 函数。如果列表为空的话会抛出 Http404 异常。


# def results(request, question_id) -> HttpResponse:
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


class IndexView(generic.ListView):
    # template_name = "polls/index.html"
    template_name = "polls/all.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]
        # Question.objects.filter(pub_date__lte=timezone.now()) returns a queryset containing Questions whose pub_date is less than or equal to - that is, earlier than or equal to - timezone.now.


class DetailView(generic.DetailView):
    model = Question
    # template_name = "polls/detail.html"
    template_name = "polls/all.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    # template_name = "polls/results.html"
    template_name = "polls/all.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    ip_address = request.META.get("REMOTE_ADDR")
    try:
        # 检查IP地址是否已经对此问题进行了投票
        # 查找具有指定问题和IP地址的 SubmittedIP 对象。如果找到了这样的对象，它将被赋值给变量 submitted_ip，否则将引发 SubmittedIP.DoesNotExist 异常。
        submitted_ip = SubmittedIP.objects.get(question=question, ip_address=ip_address)
        return render(
            request,
            "polls/all.html",
            {
                "question": question,
                "error_message": "You have already voted for this question.",
            },
        )
    except SubmittedIP.DoesNotExist:

        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])  # type: ignore
        except (KeyError, Choice.DoesNotExist):
            return render(
                request,
                "polls/all.html",
                {
                    "question": question,
                    "error_message": "You didn't select a choice.",
                },
            )
        else:
            # 增加选项的投票数，并记录IP地址投票信息
            selected_choice.votes = F("votes") + 1
            selected_choice.save()
            SubmittedIP.objects.create(question=question, ip_address=ip_address)
            # 创建一个新的 SubmittedIP 对象，并将其与特定的问题和 IP 地址关联，然后将其保存到数据库中。
            return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))  # type: ignore
            # return render(request, "polls/all.html", {"question": question})
            # 重定向返回的状态码是302


# if "choice" not in request.POST:
#     # 如果用户未选择选项或者提交空值，则返回错误消息
#     return render(
#         request,
#         "polls/all.html",
#         {
#             "question": question,
#             "error_message": "You didn't select a choice.",
#         },
#     )


# def vote(request, question_id) -> HttpResponse:
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])  # type: ignore
#     except (KeyError, Choice.DoesNotExist):
#         return render(
#             request,
#             "polls/all.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes = F("votes") + 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))  # type: ignore


# def vote(request, question_id) -> HttpResponse:
#     # return HttpResponse("You're voting on question %s." % question_id)

#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         # type: ignore
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])  # type: ignore
#         # request.POST 是一个类字典对象，让你可以通过关键字的名字获取提交的数据。 这个例子中， request.POST['choice'] 以字符串形式返回选择的 Choice 的 ID。 request.POST 的值永远是字符串。
#         # 注意，Django 还以同样的方式提供 request.GET 用于访问 GET 数据 —— 但我们在代码中显式地使用 request.POST ，以保证数据只能通过 POST 调用改动。
#         # 如果在 request.POST['choice'] 数据中没有提供 choice ， POST 将引发一个 KeyError 。上面的代码检查 KeyError ，如果没有给出 choice 将重新显示 Question 表单和一个错误信息。
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             # "polls/detail.html",
#             "polls/all.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         # else 语句在 try 语句中没有引发异常时执行，用于执行正常的逻辑，例如，如果需要在没有异常发生时执行某些代码。
#         # finally 语句（可选）在无论异常是否发生都执行，通常用于执行清理操作，比如关闭文件或释放资源。
#         selected_choice.votes = F("votes") + 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))  # type: ignore
#         # 正如上面的 Python 注释指出的，在成功处理 POST 数据后，你应该总是返回一个 HttpResponseRedirect。这不是 Django 的特殊要求，这是那些优秀网站在开发实践中形成的共识。

#         # 在这个例子中，我们在 HttpResponseRedirect 的构造函数中使用 reverse() 函数。这个函数避免了我们在视图函数中硬编码 URL。它需要我们给出我们想要跳转的视图的名字和该视图所对应的 URL 模式中需要给该视图提供的参数。 在本例中，使用在 教程第 3 部分 中设定的 URLconf， reverse() 调用将返回一个这样的字符串：

#         # "/polls/3/results/"
#         # 其中 3 是 question.id 的值。重定向的 URL 将调用 'results' 视图来显示最终的页面。


# 这是 Django 中最简单的视图。如果想看见效果，我们需要将一个 URL 映射到它——这就是我们需要 URLconf 的原因了。

# 要在 polls 目录中创建一个 URL 配置，请创建一个名为 urls.py 的文件。现在你的应用程序目录应该如下所示：

# polls/
#     __init__.py
#     admin.py
#     apps.py
#     migrations/
#         __init__.py
#     models.py
#     tests.py
#     urls.py
#     views.py
