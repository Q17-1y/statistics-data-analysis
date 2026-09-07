"""描述性统计入门示例：均值、中位数、方差与可视化"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 模拟一组学生考试成绩
np.random.seed(42)
scores = np.random.normal(loc=75, scale=10, size=100).round(1)

df = pd.DataFrame({"score": scores})

# 描述性统计
print(df["score"].describe())

# 直方图
plt.hist(scores, bins=15, color="steelblue", edgecolor="white")
plt.title("Exam Scores Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig("score_histogram.png", dpi=100)
plt.show()
