import pandas as pd

def read_excel(file_path):
    """读取Excel文件"""
    return pd.read_excel(file_path)

def write_excel(df, file_path):
    """将DataFrame写入Excel文件"""
    df.to_excel(file_path, index=False, engine='openpyxl')

def reformat_data(input_path, output_path):
    """读取成本01.xlsx，然后按照作物编号和地块类型重新整理数据"""
    # 读取数据
    data = read_excel(input_path)

    # 确保必要的列存在
    if set(['种植地块', '作物编号', '种植成本/(元/亩)']).issubset(data.columns):
        # 将作物编号设置为行，地块类型设置为列
        data.set_index(['作物编号', '种植地块'], inplace=True)
        data['种植成本/(元/亩)'].unstack(level='种植地块').to_excel(output_path, engine='openpyxl')
        print("文件已成功生成")
    else:
        raise ValueError("缺少必要的列")

# 主函数
if __name__ == "__main__":
    input_file = '成本01.xlsx'  # 输入文件路径
    output_file = '重新整理的成本.xlsx'  # 输出文件路径
    reformat_data(input_file, output_file)