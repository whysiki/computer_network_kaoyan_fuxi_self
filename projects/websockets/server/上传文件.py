from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# 设置文件上传的目录
UPLOAD_FOLDER = "./res"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/upload", methods=["POST"])  # type: ignore
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"})
    # 将给定的参数序列化为JSON，并返回a
    # ~瓶。使用application/json mime类型的响应对象。从视图返回的字典或列表将自动转换为JSON响应，而不需要调用它。
    # 这需要一个活动请求或应用程序上下文，并调用app.json.response() <flask.json.provider.JSONProvider.response>。
    # 在调试模式下，输出使用缩进格式化，以使其更易于阅读。这也可以由提供商控制。
    # 只能给出位置参数或关键字参数，不能两者都给出。如果没有给出参数，None为seri
    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"})

    if file:
        filename = secure_filename(file.filename)  # type: ignore
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return jsonify({"message": "File uploaded successfully", "filename": filename})


if __name__ == "__main__":
    app.run(debug=True, port=64444)
# 在本地开发服务器上运行应用程序。

# 不要在生产环境中使用run()。它并不打算满足生产服务器的安全性和性能需求。
# 相反，请参见/ deployment /index获取WSGI服务器建议。

# 如果设置了调试标志，服务器将自动重新加载代码更改，并在发生异常时显示调试器。

# 如果您希望在调试模式下运行应用程序，但在交互式调试器上禁用代码执行，则可以将use_evalex=False作为参数传递。这将使调试器的回溯屏幕保持活动状态，但禁用代码执行。

# 不建议将此函数用于自动重新加载的开发，因为它不支持。相反，你应该
# 使用flask命令行脚本的运行支持。

# 参数host:要监听的主机名。将其设置为“0.0.0.0”至
# 也要让服务器在外部可用。默认为'127.0.0.1'或SERVER_NAME配置变量中的主机(如果存在)。
# :param port: webserver的端口号。默认为5000或
# 在SERVER_NAME配置变量中定义的端口(如果存在)。
# 参数debug:如果给出，则启用或禁用调试模式。看到
# 调试。
# :param load_dotenv:加载最近的。env和。flaskenv
# 设置环境变量的文件。还将工作目录更改为包含找到的第一个文件的目录。
# param options:要转发到底层workzeug的选项
# 服务器。有关更多信息，请参见werkzeug. services .run_simple。
