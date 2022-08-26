import tkinter as tk
root=tk.Tk()
root.geometry("800x500+100+100")
root.title('记事本')
# caidan
menu=tk.Menu(root,tearoff=False)

file_menu=tk.Menu(menu,tearoff=False)
file_menu.add_command(label='新建')
file_menu.add_command(label='打开')
file_menu.add_command(label='保存')
file_menu.add_command(label='另存为')
menu.add_cascade(label='文件',menu=file_menu)


edit_menu=tk.Menu(menu,tearoff=False)
edit_menu.add_command(label='撤销')
edit_menu.add_command(label='重做')
edit_menu.add_separator()
edit_menu.add_command(label='粘贴')
edit_menu.add_command(label='复制')
menu.add_cascade(label='编辑',menu=edit_menu)

about_menu=tk.Menu(menu,tearoff=False)
about_menu.add_command(label='版权')
about_menu.add_command(label='作者')
menu.add_cascade(label='编辑',menu=about_menu)
root.config(menu=menu)
#
status_str_var=tk.StringVar()
status_str_var.set('字符数: %s'%0)
status_label=tk.Label(root,textvariable=status_str_var,bd=1,relief=tk.SUNKEN,anchor=tk.W)
status_label.pack(side=tk.BOTTOM,fill=tk.X)

var_line=tk.StringVar()
line_label=tk.Label(root,textvariable=var_line,width=1,bg='#faebd7',anchor=tk.N)
line_label.pack(side=tk.LEFT,fill=tk.Y)

text_pad=tk.Text(root,font=10,fg='blue')
text_pad.pack(fill=tk.BOTH,expand=True)

scroll=tk.Scrollbar(text_pad)
text_pad.config(yscrollcommand=scroll.set)
scroll.config(command=text_pad.yview)
scroll.pack(side=tk.RIGHT,fill=tk.Y)
root.mainloop()