# # # # # import subprocess as s

# # # # # ps = s.check_output(["where", "python"]).decode("utf-8")
# # # # # print(ps)

# # # # # import os

# # # # # pt = os.environ.get("PYTHONHOME")
# # # # # print(pt)
# # # # import os

# # # # p = os.__file__
# # # # d = os.path.dirname(p)
# # # # fs = os.listdir(d)
# # # # print(fs.__len__())
# # # # print(*[f'{a.split(".")[0]},' for a in fs][:10])
# # # # # ds = r"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin".split(":")
# # # # # a = []
# # # # # for d in ds:
# # # # #     for r, d, f in os.walk(d):
# # # # #         a.extend(f)
# # # # # s = set(a)


# # # # # for file in files:
# # # # #     f, ft = os.path.splitext(file)
# # # # #     print(f"{f}{ft}")
# # # # # /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# # # # # import os

# # # # # es = os.environ
# # # # # print(es.get("PATH"))
# # # # # for k, v in es.items():
# # # # #     print(f"{k}: {v}")
# # # import pip
# # # import datetime

# # # # 获取已安装库的信息
# # # installed_packages = pip.get_installed_distributions()
# # # package_info = []

# # # for package in installed_packages:
# # #     package_name = package.key
# # #     package_version = package.version
# # #     package_location = package.location

# # #     # 获取库的安装时间
# # #     timestamp = datetime.datetime.fromtimestamp(
# # #         package.location.stat().st_ctime
# # #     ).strftime('%Y-%m-%d %H:%M:%S')

# # #     package_info.append((package_name, package_version, timestamp))

# # # # 根据安装时间排序
# # # sorted_packages = sorted(package_info, key=lambda x: datetime.datetime.strptime(x[2], '%Y-%m-%d %H:%M:%S'), reverse=True)

# # # # 打印排序后的结果
# # # for package in sorted_packages:
# # #     print(f"库名: {package[0]}, 版本: {package[1]}, 安装时间: {package[2]}")
# # import pkg_resources
# # import datetime

# # # 获取已安装库的信息
# # installed_packages = list(pkg_resources.working_set)
# # package_info = []

# # for package in installed_packages:
# #     package_name = package.project_name
# #     package_version = package.version
# #     package_location = package.location

# #     # 获取库的安装时间
# #     timestamp = datetime.datetime.fromtimestamp(
# #         package_location.stat().st_ctime
# #     ).strftime('%Y-%m-%d %H:%M:%S')

# #     package_info.append((package_name, package_version, timestamp))

# # # 根据安装时间排序
# # sorted_packages = sorted(package_info, key=lambda x: datetime.datetime.strptime(x[2], '%Y-%m-%d %H:%M:%S'), reverse=True)

# # # 打印排序后的结果
# # for package in sorted_packages:
# #     print(f"库名: {package[0]}, 版本: {package[1]}, 安装时间: {package[2]}")
# import pkg_resources
# import os
# import datetime

# # 获取已安装库的信息
# installed_packages = list(pkg_resources.working_set)
# package_info = []

# for package in installed_packages:
#     package_name = package.project_name
#     package_version = package.version
#     package_location = package.location

#     # 获取库的安装时间
#     timestamp = datetime.datetime.fromtimestamp(
#         os.path.getctime(package_location)
#     ).strftime('%Y-%m-%d %H:%M:%S')

#     package_info.append((package_name, package_version, timestamp))

# # 根据安装时间排序
# sorted_packages = sorted(package_info, key=lambda x: datetime.datetime.strptime(x[2], '%Y-%m-%d %H:%M:%S'), reverse=True)

# # 打印排序后的结果
# for package in sorted_packages:
#     print(f"库名: {package[0]}, 版本: {package[1]}, 安装时间: {package[2]}")
