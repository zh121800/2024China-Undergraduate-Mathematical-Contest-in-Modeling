import matplotlib.pyplot as plt

# 设置matplotlib支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 数据
years = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
wheat_acres = [252.5335738*0.98, 253.54151679999998*0.94, 251.745492900000020*0.98, 259.4211814*0.90, 252.6923624*0.93, 252.8413126*0.94, 255.66262500000002*0.92]
crop_acres = [159.84401880000001, 144.36910849999998*1.2, 144.3981038*1.2, 152.2027355*1.22, 144.6399438*1.22, 148.3499991*1.23, 144.0219377*1.24]

# 创建折线图
plt.figure(figsize=(10, 5))  # 设置图形大小

# 绘制小麦种植面积的折线图
plt.plot(years, wheat_acres, marker='o', linestyle='-', color='b', label='小麦种植面积')

# 绘制其他作物种植面积的折线图
plt.plot(years, crop_acres, marker='s', linestyle='--', color='r', label='玉米种植面积')

# 添加图例
plt.legend()

# 添加标题和标签
plt.title('2024至2030年农作物种植面积')  # 图形标
plt.savefig('acres.png', dpi=300)
plt.show()