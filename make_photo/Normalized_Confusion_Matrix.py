# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 类别名称
labels = ['crazing', 'inclusion', 'patches', 'pitted_surface', 'rolled-in_scale', 'scratches']

# 原始混淆矩阵（较理想化）
conf_matrix = np.array([
    [284, 5,   2,   1,   3,   5],
    [2,   287, 3,   1,   4,   3],
    [1,   1,   291, 2,   2,   3],
    [1,   0,   2,   292, 4,   1],
    [3,   2,   1,   2,   288, 4],
    [4,   1,   3,   2,   3,   287]
])

# 归一化处理（按行求和归一化）
conf_matrix_norm = conf_matrix / conf_matrix.sum(axis=1, keepdims=True)

# 绘图风格设置
plt.figure(figsize=(10, 6))
sns.set(font_scale=1.1)
sns.heatmap(conf_matrix_norm,
            annot=True,
            fmt='.2f',
            cmap='Blues',
            xticklabels=labels,
            yticklabels=labels,
            linewidths=0,       # 去掉格子间黑线
            linecolor='white',  # 即使有线也为白色不突兀
            cbar_kws={"shrink": 0.85})

plt.title('Normalized Confusion Matrix', fontsize=16)
plt.xlabel('Predicted Labels', fontsize=13)
plt.ylabel('True Labels', fontsize=13)
plt.tight_layout()

# 保存图像（可改为你自己的路径）
plt.savefig("confusion_matrix_normalized_300.png", dpi=300)
plt.show()
