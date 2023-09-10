from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import time


def nodefined():
    pass
#打开文件函数
def openfile():
    filename=filedialog.askopenfilename()
    f=open(filename,'r')
    f2=f.read()
    f.close()
    text.insert(INSERT,f2)
#保存文件函数
def savefileas():
    filename=filedialog.asksaveasfilename(filetypes=[("TXT",".txt")])
    with open(filename,'a') as f:
        f.write(text.get())

def printf():
    messagebox.showerror("错误", "没有连接打印机")
#退出文档函数
def quit():
    root.destroy()

def about():
    messagebox.showinfo("关于","开发者：Change")


root=Tk()
root.title("自制文字编辑器")

def callback():
    text.edit_undo()


#右键菜单显示函数
def popup(event):
    popupmenu.post(event.x_root,event.y_root)

#复制功能函数
def copy():

    global content

    content=text.get(SEL_FIRST,SEL_LAST)
    return content

#剪切函数
def cut():
    global content

    content=text.get(SEL_FIRST,SEL_LAST)
    text.delete(SEL_FIRST,SEL_LAST)

    return content

#粘贴功能函数
def paste():

        text.insert(INSERT,content)

#全选文本函数
def select_all():
    pass

#删除函数
def textdelete():
    text.delete(SEL_FIRST,SEL_LAST)
    
#获取时间函数
def get_time():
    msg=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    text.insert(INSERT,msg)

#文字编辑区text
text=Text(root,width=90,height=40,selectforeground="black",undo=True,font=50)
text.pack()

def insretimage():
    filename=filedialog.askopenfilename()

    photo=PhotoImage(file=filename)
    text.image_create(INSERT,image=photo)
    
    mainloop()
    
#顶级菜单窗口
    
topmenu=Menu(root)

#创建文件下拉菜单，添加到顶层菜单窗口
filemenu=Menu(topmenu,tearoff=False)

#添加下拉内容：

filemenu.add("command",label="打开",command=openfile)
filemenu.add_command(label="保存",command=savefileas)
filemenu.add_command(label="另存为",command=savefileas)
filemenu.add_separator()
filemenu.add_command(label="页面设置",command=nodefined)
filemenu.add_command(label="打印",command=printf)
filemenu.add_separator()
filemenu.add_command(label="退出",command=quit)
topmenu.add_cascade(label="文件", menu=filemenu)

#创建编辑菜单
editmenu=Menu(topmenu,tearoff=False)

#创建编辑下拉内容
editmenu.add_command(label="插入图片",command=insretimage)
editmenu.add_separator()
editmenu.add_command(label="撤销",command=callback)
editmenu.add("command",label="剪切",command=cut)
editmenu.add_command(label="复制",command=copy)
editmenu.add_command(label="粘贴",command=paste)

editmenu.add_separator()
editmenu.add_command(label="查找",command=nodefined)
editmenu.add_command(label="替换",command=nodefined)
editmenu.add_command(label="转到",command=nodefined)
editmenu.add_separator()
editmenu.add_command(label="全选",command=select_all)
editmenu.add_command(label="时间/日期",command=get_time)

topmenu.add_cascade(label="编辑",menu=editmenu)

#创建格式菜单
formatmenu=Menu(topmenu,tearoff=False)
formatmenu.add_checkbutton(label="自动换行",command=nodefined)
formatmenu.add_command(label="字体",command=nodefined)
topmenu.add_cascade(label="格式",menu=formatmenu)

#查看菜单
viewmenu=Menu(topmenu,tearoff=False)

viewmenu.add_command(label="查看状态栏",command=callback)
topmenu.add_cascade(label="查看",menu=viewmenu)

#创建帮助菜单
helpmenu=Menu(topmenu,tearoff=False)
helpmenu.add_command(label="查看帮助",command=callback)
helpmenu.add_separator()
helpmenu.add_command(label="关于笔记本",command=about)

topmenu.add_cascade(label="帮助",menu=helpmenu)

#右键菜单栏
popupmenu=Menu(root,tearoff=False)
popupmenu.add_command(label="保存",command=savefileas)
popupmenu.add_command(label="另存为",command=savefileas)
popupmenu.add_separator()
popupmenu.add_command(label="全选",command=select_all)
popupmenu.add_command(label="插入",command=insretimage)
popupmenu.add_command(label="撤回",command=callback)
popupmenu.add_separator()
popupmenu.add("command",label="剪切",command=cut)
popupmenu.add_command(label="复制",command=copy)
popupmenu.add_command(label="粘贴",command=paste)
popupmenu.add("command",label="删除",command=textdelete)
text.bind("<Button-3>",popup)

#跟窗口显示菜单栏
root.config(menu=topmenu)


mainloop()
