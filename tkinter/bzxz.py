import tkinter as tk
import bzsp
import bzplun
import bzdmu
import ctypes
whnd = ctypes.windll.kernel32.GetConsoleWindow()
if whnd != 0:
    ctypes.windll.user32.ShowWindow(whnd, 0)
    ctypes.windll.kernel32.CloseHandle(whnd)
bz0=bzsp.BzSpider()
bz1=bzplun.BzSpider()
bz2=bzdmu.BzSpider()
root = tk.Tk()
root.title('哔哩哔哩下载器')
root.geometry("330x75+100+100")
def download1():
    bz0.start(search_va.get())
def download2():
    bz1.start(search_va.get(),pl_va.get())
def download3():
    bz2.start(search_va.get())
search_va = tk.Variable()
pl_va = tk.Variable()
search_bar = tk.Entry(root, textvariable=search_va)
search_bar.grid(padx=1, pady=4,row=1, column=1)
pl_bar = tk.Entry(root, textvariable=pl_va,width=10)
pl_bar.grid(padx=1, pady=4,row=1, column=2)
tk.Label(root, text='BV号和页数:', font=('黑体', 12)).grid(padx=1, pady=4,row=1, column=0)
tk.Button(root, text='视频下载', font=('黑体', 12), command=download1).grid(padx=1, pady=4,row=2, column=0)
tk.Button(root, text='弹幕下载', font=('黑体', 12), command=download3).grid(padx=1, pady=4,row=2, column=1)
tk.Button(root, text='评论下载', font=('黑体', 12), command=download2).grid(padx=1, pady=4,row=2, column=2)
root.resizable(False,False)
root.mainloop()