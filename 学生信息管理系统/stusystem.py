# 0   退出系统
# 1   录入学生信息,调用insert()函数
# 2   杳找学生信息,调用search()函数
# 3   删除学生信息,调用delete()函数
# 4   修改学生信息,调用modify()函数
# 5   对学生成绩排序,调用sort()函数
# 6   统计学生总人数,调用total()函数
# 7   显示所有的学生信息,调用show()函数
import os
filename='student.txt'
def menu():
    print('==========================学生信息管理系系统==========================')
    print('------------------------------菜单功能------------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出')
    print('-------------------------------------------------------------------')
def main():
    while True:
        menu()
        choice=int(input('请选择：'))
        if choice in [int(i) for i in range(0,8)]:
            if choice==0:
                answer=input('您确定要退出系统吗？y/n\n')
                if answer == 'y' or answer=='Y':
                    print('谢谢您的使用')
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delect()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()
def insert():
    student_list=[]
    while True:
        id=input('请输入ID(如1001):')
        if not id:
            continue
        name = input('请输入姓名:')
        if not name:
            continue
        try:
            english=int(input('请输入英语成绩:'))
            python=int(input('请输入python成绩:'))
            java=int(input('请输入java成绩:'))
        except:
            print('输入无效，不是整数类型，请重新输入:')
            continue
        student={
            'id':id,
            'name':name,
            'english':english,
            'python':python,
            'java':java,
        }
        student_list.append(student)
        answer=input('是否继续添加？y/n\n')
        if answer=='y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完毕！！！')
def save(lst):
     stu_txt=open(filename,'a',encoding='utf-8')
     for i in lst:
         stu_txt.write(str(i)+'\n')
     stu_txt.close()
def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按id查找请输入1,按姓名查找请输入2：')
            if mode=='1':
                id=input('输入学生ID')
            elif mode=='2':
                name=input('请输入学生姓名')
            else:
                print('您的输入有误，请重新输入')
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student_old=rfile.readlines()
                for i in student_old:
                    d=dict(eval(i))
                    if id !='':
                        if d['id']==id:
                            student_query.append(d)
                    elif name !='':
                        if d['name']==name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer = input('是否继续查询？y/n\n')
            if answer == 'y':
                continue
            else:
                break
        else:
            print('请先录入信息')
            break
def show_student(lst):
    if len(lst)==0:
        print('没有查到该学生数据')
        return
    format_tile = '{:^6}\t{: ^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_tile.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩','总成绩'))
    format_data = '{:^6}\t{: ^12}\t{:^8}\t{:^8}\t{:^8}\t{:^10}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english')+item.get('python')+item.get('java'))
                                 ))
def delect():
    while True:
        student_id=input('请输入要删除学生的ID: ')
        if student_id !='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False #标记是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'ID为{student_id}的学生信息已删除')
                    else:
                        print(f'没有ID为{student_id}的学生信息')
            else:
                print('暂无学生信息，请先录入')
                break
            show()
            answer=input('是否继续删除？y/n')
            if answer=='y':
                continue
            else:
                break
        else:
            print('请输入有效ID')
            continue
def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id=input('输入要修改学生的ID:')
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d['id']==student_id:
                print('找到了学生的信息，可以修改他的相关信息了！！')
                while True:
                    try:
                        d['name']=input('请输入姓名：')
                        d['english']=int(input('请输入英语成绩：'))
                        d['python']=int(input('请输入python成绩：'))
                        d['java']=int(input('请输入java成绩：'))
                    except:
                        print('输入有误，重新输入！！！')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功')
            else:
                wfile.write(str(d) + '\n')
    answer=input('是否继续修改其他学生信息？y/n\n')
    if answer=='y':
        modify()
def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as fp:
            student_list=fp.readlines()
        student_new=[]
        for i in student_list:
            d=dict(eval(i))
            student_new.append(d)
    else:
        return
    sort_way=input('请选择(0升序，1降序)')
    if sort_way=='0':
        sort_way_bool=False
    elif sort_way=='1':
        sort_way_bool = True
    else:
        print('输入错误，请重新输入')
        sort()
    mode=input('请选择排序方式（0.按学号排序；1.按英语排序；2.按python排序；3.按java排序；4.按总成绩排序）')
    if mode=='1':
        student_new.sort(key=lambda x:int(x['english']), reverse=sort_way_bool)
    elif mode=='0':
        student_new.sort(key=lambda x: int(x['id']), reverse=sort_way_bool)
    elif mode=='2':
        student_new.sort(key=lambda x:int(x['python']), reverse=sort_way_bool)
    elif mode=='3':
        student_new.sort(key=lambda x:int(x['java']), reverse=sort_way_bool)
    elif mode=='4':
        student_new.sort(key=lambda x:int(x['english']+x['python']+x['java']), reverse=sort_way_bool)
    else:
        print('输入有误，请重新输入！！！')
        sort()
    show_student(student_new)
def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as file:
            student_old=file.readlines()
            if student_old:
                print(f'一共有{len(student_old)}名学生')
            else:
                print('目前还没有录入学生信息')
    else:
        print('暂未保存数据信息.....')
def show():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as file:
            student_old=file.readlines()
            for i in student_old:
                student_lst.append(eval(i))
            if student_lst:
                show_student(student_lst)
            else:
                print('目前还没有录入学生信息')
    else:
        print('暂未保存数据信息.....')

if __name__ == '__main__':
    main()

