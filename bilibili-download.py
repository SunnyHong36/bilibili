import easygui
import os
ynbox=easygui.ynbox('选择下载方式','bilibili下载',('AV号下载','链接下载'))
if ynbox == True:
    b=easygui.enterbox(msg='输入AV号', title='bilibili下载', strip=True, image=None, root=None)
    c='python -m you_get -d -l -o /home/mwx/视频/bilibili https://www.bilibili.com/video/'+b
    print(c)
    os.system(c)
elif ynbox == False:
    d=easygui.enterbox(msg='输入连接', title='bilibili下载', strip=True, image=None, root=None)
    g=float(len(d))
    if g > 45 :
        e=d[0:d.rfind('?', 1)]
    elif g < 50 :
        e=d
    f='python -m you_get -d -l -o E:\lenovo\py '+e
    print(f)
    os.system(f)
