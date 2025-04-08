import pandas as pd

# 假设您的Excel文件的路径是 '面积.xlsx' 和 '附件2(1)1.xlsx'
import pandas as pd
# 定义文件路径
file_path = '附件2(1)1.xlsx'

# 读取Excel文件
df = pd.read_excel(file_path)
# 提取农作物编号和种植地编号
crop_ids = df['作物编号'].tolist()
plot_ids = df['地块编号'].tolist()
areas = df['种植面积/亩'].tolist()
# 初始化42*55的二维数组，所有值均为0
crops = 42
plots = 55
farm_array = [[0 for _ in range(plots)] for _ in range(crops)]

# 假设您已经有了作物编号、地块编号和种植面积的数据列表
# 这里使用示例数据，您需要替换为实际从文件中读取的数据
# 填充二维数组
for crop_id, plot_id, area in zip(crop_ids, plot_ids, areas):
    farm_array[crop_id - 1][plot_id - 1] = area

# 创建DataFrame
df = pd.DataFrame(farm_array)

# 保存到Excel文件
file_path = 'farm_data.xlsx'  # 您可以修改文件路径和名称
df.to_excel(file_path, index=False, header=False)

print(f'Excel文件已生成在路径：{file_path}')
