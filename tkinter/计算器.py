import tkinter as tk
import ctypes
whnd = ctypes.windll.kernel32.GetConsoleWindow()
if whnd != 0:
    ctypes.windll.user32.ShowWindow(whnd, 0)
    ctypes.windll.kernel32.CloseHandle(whnd)
root=tk.Tk()
root.geometry('295x280+150+150')
root.title('计算器')
root.attributes('-alpha',0.9)
root['background']='#ffffff'
font=('宋体',20)

result_num=tk.StringVar()
result_num.set('')
tk.Label(root,textvariable=result_num,width=20,font=font,height=2,justify=tk.LEFT,anchor=tk.SE).grid(row=1,column=1,columnspan=4)

button_clear=tk.Button(root,text='C',font=('宋体',16),width=5,relief=tk.FLAT,bg='#b1b2b2')
button_clear.grid(row=2,column=1,padx=4,pady=2)
button_back=tk.Button(root,text='←',font=('宋体',16),width=5,relief=tk.FLAT,bg='#b1b2b2')
button_back.grid(row=2,column=2,padx=4,pady=2)
button_division=tk.Button(root,text='/',font=('宋体',16),width=5,relief=tk.FLAT,bg='#b1b2b2')
button_division.grid(row=2,column=3,padx=4,pady=2)
button_multiplication=tk.Button(root,text='x',font=('宋体',16),width=5,relief=tk.FLAT,bg='#b1b2b2')
button_multiplication.grid(row=2,column=4,padx=4,pady=2)
button_7=tk.Button(root,text='7',font=('宋体',16),width=5,relief=tk.FLAT,bg='#eacda1')
button_7.grid(row=3,column=1,padx=4,pady=2)
button_8=tk.Button(root,text='8',font=('宋体',16),width=5,relief=tk.FLAT,bg='#eacda1')
button_8.grid(row=3,column=2,padx=4,pady=2)
button_9=tk.Button(root,text='9',font=('宋体',16),width=5,relief=tk.FLAT,bg='#eacda1')
button_9.grid(row=3,column=3,padx=4,pady=2)
button_subtraction=tk.Button(root,text='-',font=('宋体',16),width=5,relief=tk.FLAT,bg='#b1b2b2')
button_subtraction.grid(row=3,column=4,padx=4,pady=2)

button_4=tk.Button(root,text='4',font=('宋体',16),width=5,relief=tk.FLAT,bg='#eacda1')
button_4.grid(row=4,column=1,padx=4,pady=2)
button_5=tk.Button(root,text='5',font=('宋体',16),width=5,relief=tk.FLAT,bg='#eacda1')
button_5.grid(row=4,column=2,padx=4,pady=2)
button_6=tk.Button(root,text='6',font=('宋体',16),width=5,relief=tk.FLAT,bg='#eacda1')
button_6.grid(row=4,column=3,padx=4,pady=2)
button_addition=tk.Button(root,text='+',font=('宋体',16),width=5,relief=tk.FLAT,bg='#b1b2b2')
button_addition.grid(row=4,column=4,padx=4,pady=2)

button_1=tk.Button(root,text='1',font=('宋体',16),width=5,relief=tk.FLAT,bg='#eacda1')
button_1.grid(row=5,column=1,padx=4,pady=2)
button_2=tk.Button(root,text='2',font=('宋体',16),width=5,relief=tk.FLAT,bg='#eacda1')
button_2.grid(row=5,column=2,padx=4,pady=2)
button_3=tk.Button(root,text='3',font=('宋体',16),width=5,relief=tk.FLAT,bg='#eacda1')
button_3.grid(row=5,column=3,padx=4,pady=2)
button_equal=tk.Button(root,text='=',font=('宋体',16),width=5,height=3,relief=tk.FLAT,bg='#b1b2b2')
button_equal.grid(row=5,column=4,padx=4,pady=2,rowspan=2)

button_zero=tk.Button(root,text='0',font=('宋体',16),width=12,relief=tk.FLAT,bg='#eacda1')
button_zero.grid(row=6,column=1,padx=4,pady=2,columnspan=2)
button_dian=tk.Button(root,text='.',font=('宋体',16),width=5,relief=tk.FLAT,bg='#eacda1')
button_dian.grid(row=6,column=3,padx=4,pady=2)

# 绑定事件
def click_button(x):
    result_num.set(result_num.get()+x)
button_zero.config(command=lambda :click_button('0'))
button_1.config(command=lambda :click_button('1'))
button_2.config(command=lambda :click_button('2'))
button_3.config(command=lambda :click_button('3'))
button_4.config(command=lambda :click_button('4'))
button_5.config(command=lambda :click_button('5'))
button_6.config(command=lambda :click_button('6'))
button_7.config(command=lambda :click_button('7'))
button_8.config(command=lambda :click_button('8'))
button_9.config(command=lambda :click_button('9'))
button_addition.config(command=lambda :click_button('+'))
button_subtraction.config(command=lambda :click_button('-'))
button_multiplication.config(command=lambda :click_button('*'))
button_division.config(command=lambda :click_button('/'))
button_dian.config(command=lambda :click_button('.'))
def calculation():
    opt_str=result_num.get()
    try:
        result=eval(opt_str)
    except:
        result='你有病吧！'
    result_num.set(str(result))
button_equal.config(command=calculation)
def backspace():
    opt_str = result_num.get()
    opt_str=opt_str[0:-1]
    result_num.set(str(opt_str))
button_back.config(command=backspace)
def clear():
    opt_str=''
    result_num.set(str(opt_str))
button_clear.config(command=clear)
root.resizable(False,False)
root.mainloop()
