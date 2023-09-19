import numpy
import typing
import cv2
import imageio
from tqdm import tqdm


def en_faster_git_speed(filepath: str, outputpath: str) -> None:
    class VideoCapture(cv2.VideoCapture):
        pass

    cap: VideoCapture = cv2.VideoCapture(filepath)
    frames: list = []
    while True:
        ret: bool
        frame: numpy.ndarray
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)
    cap.release()

    # 保存为新的gif图片，设置duration为0.1秒
    imageio.mimsave(outputpath, frames, "GIF", duration=0.05)
    # print(imageio.mimsave.help)


en_faster_git_speed("1.gif", "4.gif")
