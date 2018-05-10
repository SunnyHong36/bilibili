import os
a=input('把源文件拖进来:')
b=input('把输出文件夹拖进来:')[:-2]
z='1920x1080'
z=input('输入分辨率(默认1920x1080):')
x=a[:-6][1:]
c=x+'.ass'
d="'"+c+"' "
e='danmaku2ass -o '+d+'-s 1920x1080 -fn "MS PGothic" -fs 48 -a 0.8 -dm 5 -ds 5 '+a
bb='分辨率:'+z
print(bb)
aa='源文件:'+a
print(aa)
bb='输出文件:'+d
print(bb)
ee='运行指令:'+e
print(ee)
os.system(e)
