import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Ellipse
import numpy as np

# 设置matplotlib支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 步骤1: 读取Excel文件
file_path = '聚类.xls'  # 替换为你的文件路径
df = pd.read_excel(file_path)

# 步骤2: 提取需要聚类的三列数据
features = ['种植成本/(元/亩)', '销售量/斤', '平均售价']
X = df[features]

# 标准化数据，因为K-means对数据的尺度敏感
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 步骤3: 进行聚类分析
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)
labels = kmeans.labels_
df['Cluster'] = labels

# 步骤4: 可视化聚类结果
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制每个聚类的点
for i in range(3):
    cluster_data = df[df['Cluster'] == i]
    ax.scatter(cluster_data['种植成本/(元/亩)'], cluster_data['销售量/斤'], cluster_data['平均售价'], label=f'聚类 {i}')

# 绘制置信球
for i in range(3):
    cluster_data_scaled = X_scaled[df['Cluster'] == i]
    cov = np.cov(cluster_data_scaled, rowvar=False)
    eigvals, eigvecs = np.linalg.eigh(cov)
    order = np.argsort(eigvals)[::-1]
    eigvecs = eigvecs[:, order]

    angle = np.degrees(np.arctan2(eigvecs[1, 1], eigvecs[0, 1]))
    width, height = 0.1 * np.sqrt(eigvals)
    ellipse = Ellipse(kmeans.cluster_centers_[i], width, height,
                      angle, edgecolor='k', fc='None', lw=1.5, zorder=2, alpha=0.5)
    ax.add_patch(ellipse)

ax.set_xlabel('种植成本 (元/亩)')
ax.set_ylabel('销售量 (斤)')
ax.set_zlabel('平均售价')
ax.legend()
plt.title('三维聚类及置信椭圆')

# 导出图表为矢量图
plt.savefig('clustering_3d_vector.svg', format='svg')  # 导出为SVG格式
# plt.savefig('clustering_3d_vector.pdf', format='pdf')  # 或者导出为PDF格式

plt.show()