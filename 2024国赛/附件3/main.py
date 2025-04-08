import pulp

# 初始化线性规划问题
prob = pulp.LpProblem("FarmOptimization", pulp.LpMaximize)

# 假设数据
years = list(range(2024, 2031))  # 2024到2030年
seasons = [1, 2]  # 两个种植季节
crops = list(range(1, 42))  # 41种作物
fields = list(range(1, 55))  # 54块地
# 假设每种作物的预期销售量、价格、成本等数据
# 这里使用随机数或者假设值，可以根据具体情况调整
expected_sales = {c: 100 for c in crops}
prices = {c: 50 for c in crops}
costs = {(c, l, s): 10 for c in crops for l in fields for s in seasons}
yields = {(c, l): 120 for c in crops for l in fields}

# 决策变量: 每种作物在每个地块、每个季度、每年种植的面积
X = pulp.LpVariable.dicts("X", (crops, fields, seasons, years), lowBound=0, cat='Continuous')

# 目标函数1: 滞销浪费情况下的利润最大化
prob += pulp.lpSum([pulp.lpSum([pulp.lpSum([pulp.lpSum(
    [min(yields[c, l] * X[c][l][s][y], expected_sales[c]) * prices[c] - costs[c, l, s] * X[c][l][s][y]
     for c in crops] for l in fields]) for s in seasons]) for y in years])

# 目标函数2: 超过部分降价出售情况下的利润最大化
# prob += pulp.lpSum([pulp.lpSum([pulp.lpSum([pulp.lpSum(
#     [min(yields[c, l] * X[c][l][s][y], expected_sales[c]) * prices[c] +
#      max(yields[c, l] * X[c][l][s][y] - expected_sales[c], 0) * 0.5 * prices[c] - costs[c, l, s] * X[c][l][s][y]
#      for c in crops] for l in fields]) for s in seasons]) for y in years])

# 约束条件1: 作物种植面积不能超过地块总面积
field_areas = {l: 100 for l in fields}  # 假设每个地块的最大种植面积为100亩
for y in years:
    for s in seasons:
for l in fields:
    prob += pulp.lpSum([X[c][l][s][y] for c in crops]) <= field_areas[l]

# 约束条件2: 每个地块三年内至少种一次豆类作物
beans = [1, 2, 3]  # 假设1, 2, 3是豆类作物编号
for l in fields:
    for s in seasons:
for y in years[:-2]:
    prob += pulp.lpSum([X[bean][l][s][y + i] for bean in beans for i in range(3)]) >= 1

# 约束条件3: 分散性约束，某个作物不能在太多地块种植
max_field_count = 4  # 每个作物每季最多种4个地块
for y in years:
    for s in seasons:
for c in crops:
    prob += pulp.lpSum([X[c][l][s][y] > 0 for l in fields]) <= max_field_count

# 求解
prob.solve()

# 输出结果
print("Status:", pulp.LpStatus[prob.status])

for v in prob.variables():
    if v.varValue > 0:
print(v.name, "=", v.varValue)

# 输出最大利润
print("Total Profit:", pulp.value(prob.objective))
