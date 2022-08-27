import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
s1=pd.DataFrame(data={
    '学号':[1001,1002,1003],
    '语文':[56,38,47],
    '数学':[88,19,70],
    '英语':[96,78,81]
})
print(s1)
s1.to_excel('数据导出.xlsx',index=False)#index=False 不要索引
# s1.to_excel('数据导出.xlsx',index=False,sheet_name='demo1')#
print('----------------------------------------------导出到多个sheet表')
# 打开一个excel文件
work=pd.ExcelWriter('导出到多个sheet表.xlsx')
s1.to_excel(work,index=False,sheet_name='所有成绩表')#
s1[['学号','语文']].to_excel(work,index=False,sheet_name='语文成绩表')#
# 保存
work.save()






