import tkinter as tk
from tkinter import messagebox
import  random
root=tk.Tk()
root.geometry('500x300+100+100')#长x宽+x+y
root.title('辞职信')
frame1=tk.Frame(root)
frame1.pack()
tk.Label(frame1,text='去你妈的二狗子',font=35,padx=20,pady=30).pack(side=tk.LEFT,anchor=tk.N)
img=tk.PhotoImage(file='1.png')
tk.Label(frame1,image=img,padx=30,pady=30,bd=0).pack(side=tk.LEFT,anchor=tk.N)
tk.Label(frame1,text='辞职人：曲爹',font=20,height=100,anchor=tk.SE).pack(side=tk.LEFT)
yes_but=tk.Button(frame1,text='同意',font=20,height=2,width=6)
yes_but.place(relx=0.3,rely=0.8,anchor=tk.CENTER)
no_but=tk.Button(frame1,text='不同意',font=20,height=2,width=6)
no_but.place(relx=0.7,rely=0.8,anchor=tk.CENTER)
frame2=tk.Frame(root)
frame2.pack()
tk.Label(frame2,text='白天要好好读书，书里有你不知道的。\n夜晚要好好睡觉，梦里有你想要的',padx=50,pady=100,height=10,font=('黑体',18),justify=tk.LEFT,fg='red').pack()
tc=tk.Button(frame2,text='退出',font=20,height=2,width=6,command=root.quit)
tc.place(relx=0.9,rely=0.9,anchor=tk.CENTER)
def on_exit():
    messagebox.showwarning(title='提示',message='重新考虑')
root.protocol('WM_DELETE_WINDOW',on_exit)
def move(event):
    no_but.place(relx=random.random(),rely=random.random(),anchor=tk.CENTER)
no_but.bind('<Enter>',move)
def sure():
    frame1.pack_forget()
    frame2.pack()
yes_but.config(command=sure)
root.mainloop()
