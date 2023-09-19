import numpy
import cv2
import imageio
from tqdm import tqdm


def en_faster_git_speed(filepath: str, outputpath: str) -> None:
    # 读取gif图片
    cap = cv2.VideoCapture(filepath)
    frames: list = []
    while True:
        ret, frame = cap.read()
        print(ret)
        if not ret:
            break
        # 将BGR格式转换为RGB格式
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        print(type(frame))
        frames.append(frame)
    cap.release()

    # 保存为新的gif图片，设置duration为0.1秒
    imageio.mimsave(outputpath, frames, "GIF", duration=0.06)
    # print(imageio.mimsave.help)


en_faster_git_speed("1.gif", "3.gif")
