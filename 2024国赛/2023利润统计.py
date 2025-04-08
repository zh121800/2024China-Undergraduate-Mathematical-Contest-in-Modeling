import pandas as pd

# 读取Excel文件
file_path = "附件2.2.xlsx"
df = pd.read_excel(file_path)

# 初始化列表
cost_list = []
min_price_list = []
max_price_list = []
yield_list = []
land_type_list = []
crop_name_list = []

# 遍历DataFrame，提取数据
for index, row in df.iterrows():
    cost = row['种植成本/(元/亩)']
    yield_per_mu = row['亩产量/斤']
    land_type = row['地块类型']
    crop_name = row['作物名称']

    # 检查销售单价是否为字符串类型
    if isinstance(row['销售单价/(元/斤)'], str):
        price_str = row['销售单价/(元/斤)']
        try:
            min_price, max_price = map(float, price_str.split('-'))
        except ValueError:
            min_price, max_price = 0, 0  # 如果转换失败，设置为0
    else:
        min_price, max_price = 0, 0  # 如果不是字符串，也设置为0

    cost_list.append(cost)
    min_price_list.append(min_price)
    max_price_list.append(max_price)
    yield_list.append(yield_per_mu)
    land_type_list.append(land_type)
    crop_name_list.append(crop_name)

# 计算最大利润和最小利润
max_profit_list = [(y * max_p - c) for y, max_p, c in zip(yield_list, max_price_list, cost_list) if c != 0 and max_p != 0]
min_profit_list = [(y * min_p - c) for y, min_p, c in zip(yield_list, min_price_list, cost_list) if c != 0 and min_p != 0]

# 创建一个新的DataFrame来存储最大利润和最小利润
profit_df = pd.DataFrame({
    '作物名称': crop_name_list,
    '地块类型': land_type_list,
    '最大利润': max_profit_list,
    '最小利润': min_profit_list
})

# 保存到Excel文件
output_file_path = "利润分析结果.xlsx"
profit_df.to_excel(output_file_path, index=False)

print(f"利润分析结果已保存到 '{output_file_path}'")