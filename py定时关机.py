import psutil
import os


def get_folder_size(folder_path):
    total_size = 0
    with os.scandir(folder_path) as entries:
        for entry in entries:
            if entry.is_file():
                total_size += entry.stat().st_size
            elif entry.is_dir():
                total_size += get_folder_size(entry.path)
    return total_size


def format_size(size):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0


if __name__ == "__main__":
    folder_path = "G:/迅雷下载"
    folder_size = get_folder_size(folder_path)
    formatted_size = format_size(folder_size)
    print(folder_size)
    print(formatted_size)
    #
    # print(f"The size of {folder_path} is: {formatted_size}")


# def get_file_size(file_path):
#     try:
#         # 获取文件大小（以字节为单位）
#         size_in_bytes = os.path.getsize(file_path)

#         # 将字节大小转换为更友好的格式（KB、MB、GB等）
#         size_str = convert_size(size_in_bytes)

#         return f"文件大小: {size_str}"
#     except FileNotFoundError:
#         return "文件不存在"
#     except Exception as e:
#         return f"发生错误: {e}"


# def convert_size(size_in_bytes):
#     # 二进制前缀
#     for unit in ["B", "KB", "MB", "GB", "TB"]:
#         if size_in_bytes < 1024.0:
#             break
#         size_in_bytes /= 1024.0
#     return "{:.2f} {}".format(size_in_bytes, unit)


# # 替换 'your_file_path' 为你要查看的文件路径
# file_path = "your_file_path"
# result = get_file_size(file_path)
# print(result)


# def get_network_throughput():
#     if 1:
#         # 获取所有网络接口的信息
#         net_if_stats = psutil.net_if_stats()
#         for k, v in net_if_stats.items():
#             print(f"{k}   {v}")


# # 替换 'Wi-Fi' 为你的实际网络接口名称，可以通过 psutil.net_if_stats() 查看所有接口
# result = get_network_throughput()
# print(result)


"""
(function) def net_if_stats() -> dict[str, snicstats]
这段话是关于一个函数或模块的说明，该函数或模块用于返回有关系统上安装的每个网络接口卡（NIC）的信息。
返回的信息以字典的形式呈现，其中键是NIC的名称，值是一个具有以下字段的命名元组（namedtuple）：

1. **isup（是否启用）：** 一个布尔值，表示该网络接口是否处于启用状态。如果为True，表示网络接口正在运行；如果为False，表示网络接口处于禁用状态。

2. **duplex（双工模式）：** 表示网络接口卡的双工模式。它可以是`NIC_DUPLEX_FULL`（全双工）、`NIC_DUPLEX_HALF`（半双工）或`NIC_DUPLEX_UNKNOWN`（双工模式未知）之一。全双工允许数据同时在两个方向上传输，而半双工只允许在一个方向上传输。

3. **speed（速度）：** 表示NIC的速度，以兆比特每秒（MB）为单位。如果无法确定速度（例如，对于'localhost'等特殊情况），则将其设置为0。

4. **mtu（最大传输单元）：** 表示以字节为单位的最大传输单元。MTU 是在网络通信中指定的每个数据包的最大大小。

这段说明提供了关于返回信息的结构和每个字段的含义，有助于理解函数或模块返回的数据的格式和内容。

"""
