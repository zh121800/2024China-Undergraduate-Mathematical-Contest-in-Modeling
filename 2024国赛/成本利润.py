import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 设置支持中文的字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 读取数据
file_path = '附件2.2.xlsx'  # 请根据实际文件位置修改路径
df = pd.read_excel(file_path)

# 处理销售单价，假设销售单价字段是字符串格式的区间，我们取平均值
def average_price(price_range):
    if isinstance(price_range, str):
        low, high = map(float, price_range.split('-'))
        return (low + high) / 2
    else:
        return float(price_range)

df['销售单价/(元/斤)'] = df['销售单价/(元/斤)'].apply(average_price)

# 计算每种作物的总收入和利润
df['总收入（元）'] = df['亩产量/斤'] * df['销售单价/(元/斤)']
df['利润（元/亩）'] = df['总收入（元）'] - df['种植成本/(元/亩)']
df['利润成本比'] = df['利润（元/亩）'] / df['种植成本/(元/亩)']

# 准备绘图
fig, ax1 = plt.subplots(figsize=(20, 8))  # 增加图表的宽度

# 确保作物名称是字符串类型
作物名称 = df['作物名称'].astype(str)

# 绘制成本和利润
bar_width = 0.4
index = range(len(作物名称))

ax1.bar(index, df['种植成本/(元/亩)'], width=bar_width, label='种植成本', color='blue')
ax1.bar([i + bar_width for i in index], df['利润（元/亩）'], width=bar_width, label='利润', color='green')

# 创建第二个y轴
ax2 = ax1.twinx()
# 将range对象转换为列表，并对其每个元素进行加法操作
ax2.plot([i + bar_width / 2 for i in index], df['利润成本比'], 'r-o', label='利润成本比')

# 设置图表标题和标签
ax1.set_xlabel('作物名称')
ax1.set_ylabel('成本和利润（元）')
ax2.set_ylabel('利润成本比')
ax1.set_title('各种作物的成本、利润及利润成本比')
ax1.set_xticks([i + bar_width / 2 for i in index])
ax1.set_xticklabels(作物名称, rotation=90)  # 设置标签竖直显示
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# 显示图表
plt.tight_layout()
plt.show()