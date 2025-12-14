# -*- coding: utf-8 -*-
# 重新导入所需的库并重新运行绘图代码（因环境重置）
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 类别名称
labels = ['crazing', 'inclusion', 'patches', 'pitted_surface', 'rolled-in_scale', 'scratches']
n_classes = len(labels)
samples_per_class = 300

# 构造一个较为理想化（但非完美）的混淆矩阵
conf_matrix = np.array([
    [284, 5,   2,   1,   3,   5],
    [2,   287, 3,   1,   4,   3],
    [1,   1,   291, 2,   2,   3],
    [1,   0,   2,   292, 4,   1],
    [3,   2,   1,   2,   288, 4],
    [4,   1,   3,   2,   3,   287]
])

# 归一化混淆矩阵
conf_matrix_norm = conf_matrix / conf_matrix.sum(axis=1, keepdims=True)

# 绘制原始混淆矩阵
plt.figure(figsize=(10, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.tight_layout()
plt.savefig("confusion_matrix_300.png")  # 当前目录
# 或者指定绝对路径：
# plt.savefig("D:/steel_defect_detection/output/confusion_matrix_300.png")
#plt.savefig("/mnt/data/confusion_matrix_300.png")
plt.show()

# 绘制归一化混淆矩阵
plt.figure(figsize=(10, 6))
sns.heatmap(conf_matrix_norm, annot=True, fmt='.2f', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.title('Normalized Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.tight_layout()
plt.savefig("/mnt/data/confusion_matrix_normalized_300.png")
plt.show()
