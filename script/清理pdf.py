import pathlib
import os

# 1. 获取当前目录及子目录下所有文件
def get_all_files(path):
    all_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

# 2. 获取所有pdf文件
def get_all_pdf_files(all_files):
    pdf_files = []
    for file in all_files:
        if file.endswith(".pdf"):
            pdf_files.append(file)
    return pdf_files

# 3. 清理pdf文件

def clear_pdf_files(pdf_files):
    for file in pdf_files:
        # 删除
        os.remove(file)
        print("删除文件：", file)


current_path = os.path.dirname(os.path.abspath(__file__))

parent_path = pathlib.Path(current_path).parent

all_files = get_all_files(parent_path)

pdf_files = get_all_pdf_files(all_files)

clear_pdf_files(pdf_files)