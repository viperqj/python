import pandas as pd

# 1. 准备数据
# 1.1 加载数据
datas = pd.read_json('./世界各国疫情数据.json')

# 1.2 按照当前确诊数量, 对数据进行排序, 获取从确诊数量从高到低的国家名称
datas.sort_values(by='currentConfirmedCount', ascending=False, inplace=True)
country_names = datas['countryName'].unique()

# 1.3 使用透视表,统计每一天, 每个国家的确诊人数
final_data = datas.pivot_table('confirmedIncr', index='dateId', columns='countryName')
# 调整列的顺序
final_data = final_data[country_names]

# 1.4 使用0填充缺失值
final_data.fillna(0, inplace=True)

# 1.5 把每一天, 每个国家的确诊人数写入文件
final_data.to_csv('./世界各国疫情数据.csv')
