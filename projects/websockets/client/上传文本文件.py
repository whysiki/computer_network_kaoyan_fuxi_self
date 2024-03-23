import requests
from config import HOST

# import glob
import os

# import yaml

# # 读取 YAML 文件
# with open("config.yml", "r") as file:
#     data = yaml.safe_load(file)
# 服务器上传文件的URL
upload_url = f"{HOST}/upload"


def postOneTextFile(file_path):
    """return response.json()"""
    # 打开本地文件并准备上传
    with open(file_path, "rb") as file:
        files = {"file": file}
        response = requests.post(upload_url, files=files)
    return response.json()


# 发送一个POST请求。
# :param url:新Request对象的url。
# :param data:(可选)字典，元组，字节或类文件列表
# 对象在请求体中发送。
# :param json:(可选)在请求体中发送的json数据。
# **kwargs:请求接受的可选参数。
# :返回:Response <Response>对象
# : rtype:请求。响应


def get_files_with_extension(folder_path, extension):
    # 获取文件夹中的所有文件和子文件夹
    all_files = os.listdir(folder_path)

    # 使用列表推导式筛选出所有以指定后缀结尾的文件
    files_with_extension = [
        os.path.join(folder_path, file)
        for file in all_files
        if file.endswith(extension)
    ]

    return files_with_extension


def postTextFiles(folder: str, extension: str):  # -> list[Any]:
    files = get_files_with_extension(folder, extension)

    jsons = []

    for i in files:
        jsons.append(postOneTextFile(i))

    return jsons

    # glob.glob
    #     # 返回与路径名模式匹配的路径列表。
    #     # 该模式可能包含简单的shell样式通配符，如fnmatch。然而，与fnmatch不同的是，以点开头的文件名是特殊情况，不匹配'*'和'?”模式。
    #     # 如果recursive为true，模式'**'将匹配任何文件以及零个或多个目录和子目录。
    #     print(files)


def test():
    """生成测试数据"""
    for i in range(555, 1400):
        with open(f"./res/document/text{i}.txt", "w") as f:
            f.write(f"{i}" * 20000)


test()
print(postTextFiles(os.path.join(os.getcwd(), "res", "document"), ".txt"))

# 打印服务器端的响应
# print(get_files_with_extension(os.path.join(os.getcwd(), "res", "document"), ".txt"))
