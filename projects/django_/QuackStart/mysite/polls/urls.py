from django.urls import path
from . import views

# 为 URL 名称添加命名空间
app_name = "polls"
# urlpatterns = [
#     # /polls/
#     path("", views.index, name="index"),
#     # /polls/5/
#     # question_id作为字典参数传给对应处理逻辑
#     path("<int:question_id>/", views.detail, name="detail"),
#     # /polls/5/results/
#     path("specifics/<int:question_id>/results/", views.results, name="results"),
#     # /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]
# 请注意，第二和第三个模式的路径字符串中匹配的模式名称已从 <question_id> 更改为 <pk>。这是因为我们将使用 DetailView 通用视图来替换我们的 detail() 和 results() 视图，它期望从 URL 中捕获的主键值被称为 "pk"。
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
# Main entry point for a request-response process.


# 下一步是要在根 URLconf 文件中指定我们创建的 polls.urls 模块。
# 在 mysite/urls.py 文件的 urlpatterns 列表里插入一个 include()， 如下：


# 函数 path() 具有四个参数，两个必须参数：route 和 view，两个可选参数：kwargs 和 name。现在，是时候来研究这些参数的含义了。


# path() 参数： route
# route 是一个匹配 URL 的准则（类似正则表达式）。当 Django 响应一个请求时，它会从 urlpatterns 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。

# 这些准则不会匹配 GET 和 POST 参数或域名。例如，URLconf 在处理请求 https://www.example.com/myapp/ 时，它会尝试匹配 myapp/ 。处理请求 https://www.example.com/myapp/?page=3 时，也只会尝试匹配 myapp/。

# path() 参数： view
# 当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入。稍后，我们会给出一个例子。

# path() 参数： kwargs
# 任意个关键字参数可以作为一个字典传递给目标视图函数。本教程中不会使用这一特性。

# path() 参数： name
# 为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式。

# 当你了解了基本的请求和响应流程后，请阅读 教程的第 2 部分 开始使用数据库.
