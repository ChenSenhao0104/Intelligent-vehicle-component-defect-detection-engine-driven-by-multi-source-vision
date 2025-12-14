# -*- coding: utf-8 -*-
#运行得到的信息就是自己训练好的YOLOv8模型的信息
#输出的是自己训练过的YOLOv8模型best.pt的结构信息和参数量等
#在第一次测试中得到了：Model summary: 129 layers, 3,012,018 parameters, 0 gradients, 8.2 GFLOPs
#也就是说：字段名	含义说明
#129 layers	            模型一共包含129层神经网络（卷积、激活、池化等）
#3,012,018 parameters	总共有约301万个可训练参数。这个值越高，模型容量越大，表达能力越强。
#0 gradients	        当前模型没有正在训练的梯度（你只是加载它，没有进行model.train()）
#8.2 GFLOPs	            每张图片需要进行约8.2亿次浮点运算，表示模型计算量。
from ultralytics import YOLO

# 加载你的模型
model = YOLO("models/best.pt")

# 打印模型结构信息
model.info()
#运行方式（Anaconda Prompt中）：
#cd D:\steel_defect_detection\SteelDetection\SteelDetection
#conda activate py39
#python check_model_info.py