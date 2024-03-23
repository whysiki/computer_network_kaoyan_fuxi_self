# 创建项目
如果这是你第一次使用 Django 的话，你需要一些初始化设置。也就是说，你需要用一些自动生成的代码配置一个 Django project —— 即一个 Django 项目实例需要的设置项集合，包括数据库配置、Django 配置和应用程序配置。

打开命令行，cd 到一个你想放置你代码的目录，然后运行以下命令：

```django-admin startproject mysite```



# 让我们看看 `startproject` 创建了些什么：

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

这些目录和文件的用处是：

- **最外层的 `mysite/` 根目录**：只是你项目的容器，根目录名称对 Django 没有影响，你可以将它重命名为任何你喜欢的名称。

- **`manage.py`**：一个让你用各种方式管理 Django 项目的命令行工具。你可以阅读 `django-admin` 和 `manage.py` 获取所有 `manage.py` 的细节。

- **里面一层的 `mysite/` 目录**：包含你的项目，它是一个纯 Python 包。它的名字就是当你引用它内部任何东西时需要用到的 Python 包名。 (比如 `mysite.urls`).

    - **`mysite/__init__.py`**：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。如果你是 Python 初学者，阅读官方文档中的 [更多关于包的知识](https://docs.python.org/3/tutorial/modules.html#packages)。

    - **`mysite/settings.py`**：Django 项目的配置文件。如果你想知道这个文件是如何工作的，请查看 [Django 配置](https://docs.djangoproject.com/en/3.2/topics/settings/) 了解细节。

    - **`mysite/urls.py`**：Django 项目的 URL 声明，就像你网站的“目录”。阅读 [URL调度器 文档](https://docs.djangoproject.com/en/3.2/topics/http/urls/) 来获取更多关于 URL 的内容。

    - **`mysite/asgi.py`**：作为你的项目的运行在 ASGI 兼容的 Web 服务器上的入口。阅读 [如何使用 ASGI 来部署](https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/) 了解更多细节。

    - **`mysite/wsgi.py`**：作为你的项目的运行在 WSGI 兼容的 Web 服务器上的入口。阅读 [如何使用 WSGI 进行部署](https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/) 了解更多细节。


# 用于开发的简易服务器

让我们来确认一下你的 Django 项目是否真的创建成功了。如果你的当前目录不是外层的 `mysite` 目录的话，请切换到此目录，然后运行下面的命令：

```bash
$ python manage.py runserver
```

你应该会看到如下输出：

```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

March 21, 2024 - 15:50:53
Django version 5.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

**备注:**

忽略有关未应用最新数据库迁移的警告，稍后我们处理数据库。

你已经启动了 Django 开发服务器，这是一个用纯 Python 编写的轻量级网络服务器。我们在 Django 中包含了这个服务器，所以你可以快速开发，而不需要处理配置生产服务器的问题 -- 比如 Apache -- 直到你准备好用于生产。

现在是个提醒你的好时机：千万不要 将这个服务器用于和生产环境相关的任何地方。这个服务器只是为了开发而设计的。（我们在网络框架方面是专家，在网络服务器方面并不是。）

服务器现在正在运行，通过浏览器访问 [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 。你将看到一个“祝贺”页面，有一只火箭正在发射。你成功了！

**更换端口**

默认情况下，`runserver` 命令会将服务器设置为监听本机内部 IP 的 8000 端口。

如果你想更换服务器的监听端口，请使用命令行参数。举个例子，下面的命令会使服务器监听 8080 端口：

```bash
$ python manage.py runserver 8080
```

如果你想要修改服务器监听的IP，在端口之前输入新的。比如，为了监听所有服务器的公开IP（这你运行 Vagrant 或想要向网络上的其它电脑展示你的成果时很有用），使用：

```bash
$ python manage.py runserver 0.0.0.0:8000
```

关于这个简易服务器的完整信息可以在 [runserver 文档](https://docs.djangoproject.com/en/3.2/ref/django-admin/#runserver) 中找到。

**会自动重新加载的服务器 `runserver`**

用于开发的服务器在需要的情况下会对每一次的访问请求重新载入一遍 Python 代码。所以你不需要为了让修改的代码生效而频繁的重新启动服务器。然而，一些动作，比如添加新文件，将不会触发自动重新加载，这时你得自己手动重启服务器。
