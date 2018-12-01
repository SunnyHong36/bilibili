# -*- coding: UTF-8 -*-
import webbrowser 
import easygui
a=easygui.ynbox('选择搜索方式','bilibili搜索',('AV号跳转','输入搜索'))
if a == True:
    b=easygui.enterbox(msg='输入AV号', title='bilibili搜索', strip=True, image=None, root=None)
    c='https://www.bilibili.com/video/'+b
    webbrowser.open_new(c)
elif a ==False:
    d=easygui.enterbox(msg='输入搜索内容', title='bilibili搜索', strip=True, image=None, root=None)
    e='https://search.bilibili.com/all?keyword='+d
    webbrowser.open_new(e)
