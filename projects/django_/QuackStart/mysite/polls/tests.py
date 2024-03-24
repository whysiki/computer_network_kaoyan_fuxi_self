from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question, Choice, SubmittedIP
from django.urls import reverse
from django.http import HttpRequest
from polls.views import vote  # 导入 vote 函数

# import webbrowser
from unittest.mock import patch


# python manage.py test polls
# Question
class QuestionModelTests(TestCase):
    # was_published_recently()
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)  # 期待返回False
        # Just like self.assertTrue(a is b), but with a nicer default message.

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])
        # test_no_questions 不会创建任何问题，但会检查消息 "No polls are available." 并验证 latest_question_list 是否为空。注意，django.test.TestCase 类提供了一些额外的断言方法。在这些示例中，我们使用了 assertContains() 和 assertQuerySetEqual()。

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))  # type: ignore
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))  # type: ignore
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
        # 断言响应表明成功检索了某些内容(即HTTP状态码符合预期)，并且文本在响应的内容中出现了计数次。如果count为None，则计数无关紧要—如果文本在响应中至少出现一次，则断言为真。


class VoteViewTests(TestCase):
    def test_duplicate_vote(self):
        # 创建一个问题
        question = Question.objects.create(
            question_text="Test question", pub_date=timezone.now()
        )
        # 创建两个选项
        choice1 = Choice.objects.create(question=question, choice_text="Choice 1")
        choice2 = Choice.objects.create(question=question, choice_text="Choice 2")

        # 模拟一个用户投票
        response = self.client.post(
            reverse("polls:vote", args=(question.id,)), {"choice": choice1.id}  # type: ignore
        )
        self.assertEqual(response.status_code, 302)  # 应该重定向到结果页面

        # 再次尝试使用相同的选项和IP地址进行投票
        response = self.client.post(
            reverse("polls:vote", args=(question.id,)), {"choice": choice1.id}  # type: ignore
        )
        self.assertContains(response, "You have already voted for this question.")

    def test_successful_vote(self):
        # 创建一个问题
        question = Question.objects.create(
            question_text="Test question", pub_date=timezone.now()
        )
        # 创建一个选项
        choice = Choice.objects.create(question=question, choice_text="Choice")

        # 模拟一个用户投票
        response = self.client.post(
            reverse("polls:vote", args=(question.id,)), {"choice": choice.id}  # type: ignore
        )
        self.assertEqual(response.status_code, 302)  # 应该重定向到结果页面

        # # 检查是否返回了正确的错误消息
        # self.assertEqual(response.status_code, 200)  # 应该是正常的请求成功
        # self.assertContains(response, "You didn't select a choice.")

    @patch("polls.views.render")
    def test_no_choice_selected(self, mock_render):
        # 创建一个问题
        question = Question.objects.create(
            question_text="Test question", pub_date=timezone.now()
        )
        # 创建一个选项
        choice = Choice.objects.create(question=question, choice_text="Choice")

        # 模拟一个POST请求，但没有提供选项的选择
        request = HttpRequest()
        request.method = "POST"
        response = vote(request, question.id)  # type: ignore

        # 检查是否调用了 render 函数，并且错误消息正确传递给了模板
        mock_render.assert_called_once_with(
            request,
            "polls/all.html",
            {"question": question, "error_message": "You didn't select a choice."},
        )

        # print(f"测试成功test_no_choice_selected")

    # def test_no_choice_selected(self):
    #     # 创建一个问题
    #     question = Question.objects.create(
    #         question_text="Test question", pub_date=timezone.now()
    #     )
    #     # 创建一个选项
    #     choice = Choice.objects.create(question=question, choice_text="Choice")

    #     # 模拟一个POST请求，但没有提供选项的选择
    #     request = HttpRequest()
    #     request.method = "POST"
    #     # request.POST["choice"] = ""  # 不提供选项的选择
    #     response = vote(request, question.id)  # type: ignore

    #     # 检查是否返回了正确的错误消息
    #     self.assertEqual(response.status_code, 200)  # 应该是正常的请求成功

    #     html_string = response.content.decode()
    #     with open("temp.html", "w") as f:
    #         f.write(html_string)

    #     webbrowser.open("temp.html")

    #     self.assertContains(response, "You didn't select a choice.")


# self.assertContains(
#     response, "You didn't select a choice."
# )  # 检查页面内容是否包含错误消息

# print(response.json())
# self.assertContains(response, "You didn't select a choice.")

# You didn't select a choice.

# def test_choice_not_exist(self):
#     # 创建一个问题
#     question = Question.objects.create(
#         question_text="Test question", pub_date=timezone.now()
#     )

#     # 模拟一个POST请求，但选择了不存在的选项
#     request = HttpRequest()
#     request.method = "POST"
#     request.POST["choice"] = "999"  # 选择一个不存在的选项
#     response = vote(request, question.id)  # type: ignore

#     # 检查是否返回了正确的错误消息
#     self.assertEqual(response.status_code, 200)  # 应该是正常的请求成功
#     self.assertContains(response, "You didn't select a choice.")


# def test_no_choice_selected(self):
#     # 创建一个问题
#     question = Question.objects.create(
#         question_text="Test question", pub_date=timezone.now()
#     )
#     # 创建一个选项
#     choice = Choice.objects.create(question=question, choice_text="Choice")

#     # 模拟一个用户未选择选项就尝试投票
#     response = self.client.post(reverse("polls:vote", args=(question.id,)), {})  # type: ignore

#     # 检查是否返回了正确的错误消息
#     self.assertEqual(response.status_code, 200)  # 应该是正常的请求成功
#     self.assertContains(response, "You didn't select a choice.")

#     # 创建一个问题
#     question = Question.objects.create(
#         question_text="Test question", pub_date=timezone.now()
#     )
#     # 创建一个选项
#     choice = Choice.objects.create(question=question, choice_text="Choice")

#     # 模拟一个POST请求，但没有提供选项的选择
#     request = HttpRequest()
#     request.method = "POST"
#     request.POST["choice"] = ""  # 不提供选项的选择
#     response = vote(request, question.id)

#     # 检查是否返回了正确的错误消息
#     self.assertEqual(response.status_code, 200)  # 应该是正常的请求成功
#     self.assertContains(response, "You didn't select a choice.")

# def test_no_choice_selected(self):
#     # 创建一个问题
#     question = Question.objects.create(
#         question_text="Test question", pub_date=timezone.now()
#     )
#     # 创建一个选项
#     choice = Choice.objects.create(question=question, choice_text="Choice")

#     # 模拟一个用户未选择选项就尝试投票
#     response = self.client.post(reverse("polls:vote", args=(question.id,)), {})  # type: ignore
#     print(response)
#     self.assertContains(
#         response, "You didn't select a choice."
#     )  # "You didn't select a choice."
# Assert that a response indicates that some content was retrieved successfully,
# (i.e., the HTTP status code was as expected) and that text occurs count times in the content of the response.
# If count is None, the count doesn't matter - the assertion is true if the text occurs at least once in the response.
# 断言响应表明某些内容被成功检索
# (即HTTP状态码与预期一致)，并且该文本在响应内容中出现了计数次。
# 如果count为None，则计数无关紧要—如果文本在响应中至少出现一次，则断言为真。
