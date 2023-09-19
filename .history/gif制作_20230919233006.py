import numpy as np
import cv2
import imageio

# 读取gif图片
cap = cv2.VideoCapture("input.gif")
frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # 将BGR格式转换为RGB格式
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frames.append(frame)
cap.release()

# 保存为新的gif图片，设置duration为0.1秒
imageio.mimsave("output.gif", frames, "GIF", duration=0.1)
