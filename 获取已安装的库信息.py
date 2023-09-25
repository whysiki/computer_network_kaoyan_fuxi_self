import os
import datetime
import pkg_resources
from pkg_resources import DistInfoDistribution
# p = os.__file__
# d = os.path.dirname(p)
# fs = os.listdir(d)
# print(fs.__len__())
# print(*[f'{a.split(".")[0]},' for a in fs][:10])
# ds = r"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin".split(":")
# a = []
# for d in ds:
#     for r, d, f in os.walk(d):
#         a.extend(f)
# s = set(a)

# 获取已安装库的信息


class Packages():
    class Package():
        def __init__(self,package:DistInfoDistribution) -> None:
            self.package_name = package.project_name
            self.package_version = package.version
            self.package_location = package.location
        
    def __init__(self) -> None:
        
        # self.installed_packages=list(pkg_resources.working_set)
        installed_packages = list(pkg_resources.working_set)
        package_info = []
        
        for package in installed_packages:
            package_name = package.project_name
            package_version = package.version
            package_location = package.location
            # 获取库的安装时间
            timestamp = datetime.datetime.fromtimestamp(
                os.path.getctime(package_location)
            ).strftime('%Y-%m-%d %H:%M:%S')

            package_info.append((package_name, package_version, timestamp))
            
installed_packages = list(pkg_resources.working_set)
package_info = []

for package in installed_packages:
    # print(type(package))
    package_name = package.project_name
    package_version = package.version
    package_location = package.location
    # 获取库的安装时间
    timestamp = datetime.datetime.fromtimestamp(
        os.path.getctime(package_location)
    ).strftime('%Y-%m-%d %H:%M:%S')

    package_info.append((package_name, package_version, timestamp))
# 根据安装时间排序
sorted_packages = sorted(package_info, key=lambda x: datetime.datetime.strptime(x[2], '%Y-%m-%d %H:%M:%S'), reverse=True)

def print_table(data):
    # 确定每列的最大宽度
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

    # 打印表头边框
    for width in column_widths:
        print(f"+{'-' * (width + 2)}", end="")
    print("+")

    # 打印表头
    for i, (item, width) in enumerate(zip(data[0], column_widths)):
        print(f"| {item:{width}} ", end="")
    print("|")

    # 打印表格边框
    for width in column_widths:
        print(f"+{'-' * (width + 2)}", end="")
    print("+")

    # 打印数据行
    for row in data[1:]:
        for i, (item, width) in enumerate(zip(row, column_widths)):
            print(f"| {item:{width}} ", end="")
        print("|")

    # 打印表格底部边框
    for width in column_widths:
        print(f"+{'-' * (width + 2)}", end="")
    print("+")


# 打印排序后的结果
# for package in sorted_packages:
#     print(f"库名: {package[0]}, 版本: {package[1]}, 安装时间: {package[2]}")
# 你的数据
data =  [["Module", 'Version','Last Modified']] + sorted_packages

# 调用函数打印带有边框的表格
print_table(data)
