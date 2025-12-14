# -*- coding: utf-8 -*-
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import matplotlib

# 中文支持
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 路径根据你的实际情况修改
img_path = "TestFiles/inclusion_4.jpg"
model = YOLO("models/best.pt")

results = model(img_path)[0]
annotated_img = results.plot()

original = cv2.imread(img_path)
original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
annotated = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original)
plt.title("原图")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(annotated)
plt.title("检测结果图")
plt.axis("off")

plt.savefig("detect_comparison.jpg", dpi=300)
plt.show()
