import pandas as pd

#import pandas as pd

# 读取Excel文件
df = pd.read_excel('./23年数据.xlsx')

# 创建一个全零的三维列表
field = [[[0 for _ in range(3)] for _ in range(55)] for _ in range(42)]

# 提取数据并填充field
for _, row in df.iterrows():
    x, y, z, area = row['作物编号'], row['种植地块'], row['季节编号'], row['种植面积/亩']

    # 将x, y, z转换为整数索引
    x, y, z = int(x) , int(y) , int(z)

    # 将area值填入field
    field[x][y][z] = area

# 现在field已被正确填充
print (field)