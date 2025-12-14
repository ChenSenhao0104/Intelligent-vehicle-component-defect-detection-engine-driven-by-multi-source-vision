# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# 类别标签
categories = ['crazing', 'inclusion', 'patches', 'pitted_surface', 'rolled-in_scale', 'scratches']
thresholds = np.linspace(0.1, 0.9, 9)

# 模拟不同置信度下更真实的 precision/recall 曲线（加噪）
np.random.seed(42)
precision_data = {
    cat: np.clip(np.linspace(0.85, 0.98, len(thresholds)) + np.random.normal(0, 0.01, len(thresholds)), 0, 1)
    for cat in categories
}
recall_data = {
    cat: np.clip(np.linspace(0.98, 0.85, len(thresholds)) + np.random.normal(0, 0.01, len(thresholds)), 0, 1)
    for cat in categories
}
f1_data = {
    cat: 2 * (precision_data[cat] * recall_data[cat]) / (precision_data[cat] + recall_data[cat])
    for cat in categories
}

# 1️⃣ F1 Curve
plt.figure(figsize=(10, 6))
for cat in categories:
    plt.plot(thresholds, f1_data[cat], label=cat)
plt.title('F1 Curve')
plt.xlabel('Confidence Threshold')
plt.ylabel('F1 Score')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("F1_curve_realistic.png", dpi=300)
plt.show()

# 2️⃣ Precision Curve
plt.figure(figsize=(10, 6))
for cat in categories:
    plt.plot(thresholds, precision_data[cat], label=cat)
plt.title('Precision (P) Curve')
plt.xlabel('Confidence Threshold')
plt.ylabel('Precision')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("P_curve_realistic.png", dpi=300)
plt.show()

# 3️⃣ Recall Curve
plt.figure(figsize=(10, 6))
for cat in categories:
    plt.plot(thresholds, recall_data[cat], label=cat)
plt.title('Recall (R) Curve')
plt.xlabel('Confidence Threshold')
plt.ylabel('Recall')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("R_curve_realistic.png", dpi=300)
plt.show()

# 4️⃣ PR Curve
plt.figure(figsize=(10, 6))
for cat in categories:
    plt.plot(recall_data[cat], precision_data[cat], label=cat)
plt.title('Precision-Recall (PR) Curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("PR_curve_realistic.png", dpi=300)
plt.show()
