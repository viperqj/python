#example7_9.py
#coding=gbk
import openpyxl
#��xlsx�ļ��е��빤��������
workbook = openpyxl.load_workbook('̫����ʳ�̼�����.xlsx')
#�ӹ������л����sheet��ΪԪ�ص��б�
sheetNames = workbook.sheetnames
#����ÿ��sheet
for sheetName in sheetNames:
    print('��ǰ����������Ϊ��%s'%sheetName)
    #����sheet����ȡsheet����
    sheet = workbook[sheetName]
    #����sheet�е�ÿ����Ԫ��
    for i in range(sheet.max_row):
        for j in range(sheet.max_column):
            print(sheet.cell(row=i+1, column=j+1).value,end='\t')
        print()
