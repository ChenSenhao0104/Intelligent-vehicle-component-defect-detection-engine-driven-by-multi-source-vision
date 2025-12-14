# -*- coding: utf-8 -*-
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 假设这些数据是你提供的
data = {
    'x': np.random.rand(1000),
    'y': np.random.rand(1000),
    'width': np.random.rand(1000),
    'height': np.random.rand(1000)
}

# 转换为DataFrame
df = pd.DataFrame(data)

# 计算相关性矩阵
corr = df.corr()

# 绘制热图
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="Blues", cbar=True, linewidths=0.5)

# 添加标题
plt.title('Labels Correlation Matrix')

# 显示图像
plt.show()
