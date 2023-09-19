import numpy as np
import cv2
import imageio

# 读取gif图片
cap = cv2.VideoCapture("1.gif")
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
imageio.mimsave("2.gif", frames, "GIF", duration=0.01)
# print(imageio.mimsave.help)
