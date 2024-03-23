"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
    
    mysite项目的URL配置。
    ' urlpatterns '列表将url路由到视图。更多信息请参见:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
    例子:
    功能视图
    1. 添加一个import: from my_app导入视图
    2. 在urlpatterns: path("， views. path ")中添加一个URL。家,name = '家')
    基于类的观点
    1. 添加一个import: from other_app。views import Home
    2. 添加一个URL到urlpatterns: path("， home .as_view()， name='home')
    包括另一个URLconf
    1. 从django中导入include()函数。url导入包括，路径
    2. 添加URL到u
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("polls.urls")),
    # path("", include("polls.urls")),
    # path("__debug__/", include("debug_toolbar.urls")),
]


# 函数 include() 允许引用其它 URLconfs。每当 Django 遇到 include() 时，它会截断与此项匹配的 URL 的部分，并将剩余的字符串发送到 URLconf 以供进一步处理。

# 我们设计 include() 的理念是使其可以即插即用。因为投票应用有它自己的 URLconf( polls/urls.py )，他们能够被放在 "/polls/" ， "/fun_polls/" ，"/content/polls/"，或者其他任何路径下，这个应用都能够正常工作。
