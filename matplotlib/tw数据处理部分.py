import pandas as pd
datas = pd.read_json('./tw.json')
final_data = datas.pivot_table('confirmedIncr', index='dateId')
print(final_data)
final_data.fillna(0, inplace=True)
final_data.to_csv('./tw.csv')
