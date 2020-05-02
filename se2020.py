#! /usr/bin/env python   
# -*- coding: utf-8 -*-  
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

from tkinter import *
from tkinter import messagebox
import numpy as np
import matlab.engine
from ctypes import *
import math

#调用编写的三角函数的python模块
from sin_se import sin_se_p
from cos_se import cos_se_p
from tan_se import tan_se_p
from cot_se import cot_se_p

root = Tk()

#调用matlab中m文件函数
eng = matlab.engine.start_matlab()


sv0=StringVar()    #sv0为输入
sv1=StringVar()    #sv1~4为matlab语言的输出
sv2=StringVar()
sv3=StringVar()
sv4=StringVar()
sv5=StringVar()    #sv5~8为python语言的输出
sv6=StringVar()
sv7=StringVar()
sv8=StringVar() 


#界面编写
l1=Label(text="三角函数计算",font=('KaiTi',12,'bold'))
l1.grid(row=0,column=0,columnspan=2)        #Title and Title Location

#输入网格
i1=Entry()
i1.grid(row=3,column=1)
i1.config(textvariable=sv0)
in1=Label(text="请输入：",font=('KaiTi',12,'bold'))
in1.grid(row=3,column=0)

#输出网格,matlab
in1=Label(text="matlab语言：",font=('KaiTi',12,'bold'))
in1.grid(row=4,column=0)

o1=Entry()
o1.grid(row=6,column=1)
o1.config(textvariable=sv1, state='readonly')
out1=Label(text="sin:",font=('KaiTi',12,'bold'))
out1.grid(row=6,column=0)

o2=Entry()
o2.grid(row=7,column=1)
o2.config(textvariable=sv2, state='readonly')
out2=Label(text="cos:",font=('KaiTi',12,'bold'))
out2.grid(row=7,column=0)

o3=Entry()
o3.grid(row=8,column=1)
o3.config(textvariable=sv3, state='readonly')
out3=Label(text="tan:",font=('KaiTi',12,'bold'))
out3.grid(row=8,column=0)

o4=Entry()
o4.grid(row=9,column=1)
o4.config(textvariable=sv4, state='readonly')
out4=Label(text="cot:",font=('KaiTi',12,'bold'))
out4.grid(row=9,column=0)

#输出网格,python
in1=Label(text="python语言：",font=('KaiTi',12,'bold'))
in1.grid(row=10,column=0)

o5=Entry()
o5.grid(row=11,column=1)
o5.config(textvariable=sv5, state='readonly')
out5=Label(text="sin:",font=('KaiTi',12,'bold'))
out5.grid(row=11,column=0)

o6=Entry()
o6.grid(row=12,column=1)
o6.config(textvariable=sv6, state='readonly')
out6=Label(text="cos:",font=('KaiTi',12,'bold'))
out6.grid(row=12,column=0)

o7=Entry()
o7.grid(row=13,column=1)
o7.config(textvariable=sv7, state='readonly')
out7=Label(text="tan:",font=('KaiTi',12,'bold'))
out7.grid(row=13,column=0)

o8=Entry()
o8.grid(row=14,column=1)
o8.config(textvariable=sv8, state='readonly')
out8=Label(text="cot:",font=('KaiTi',12,'bold'))
out8.grid(row=14,column=0)


#button function,角度/弧度的转换
def h1():         #Angle and radian control button
    if bt1['text']=='弧度':
        bt1['text']='角度'

    else:
        bt1['text']='弧度'


#radian = float(sv0.get()) * np.pi/180

#实现计算
def h2():
    if (sv0.get() == ""):
        messagebox.showwarning(title='FBI Warning', message='PLEASE INPUT A NUMBER！')
    else:
        try:
            str = float(sv0.get())
            str = str % 360
        except:
            messagebox.showerror(title='Error', message='请输入 < 99999999的数')

    if bt1['text']=='弧度':
        str = str * (180/np.pi)     #所有函数输入角度，这里进行弧度角度转换
    sv1.set(eng.m_sin_se(str))    #1~4matlab输出值
    sv2.set(eng.cos_se(str))
    sv3.set(eng.m_tan_se(str))
    sv4.set(eng.m_cot_se(str))
    
    sv5.set(sin_se_p(str))      #5~8python输出值
    sv6.set(cos_se_p(str))
    sv7.set(tan_se_p(str))
    sv8.set(cot_se_p(str))


bt1=Button(root,text='角度',font=('KaiTi',12,'bold'),width=5,height=2,command=h1)
bt1.grid(row=1,column=0,sticky='e')


bt2=Button(text="计算",font=('KaiTi',12,'bold'),width=5,height=2, command=h2)
bt2.grid(row=1,column=1,sticky='e')

#--------------------------
from Test_cos_se import test_cos
from Test_sin_se import test_sin
from Test_tan_se import test_tan
from Test_cot_se import test_cot

#清除所有界面的信息
def clear_all():
    sv0.set("")

    sv1.set("")  # 1~4matlab输出值
    sv2.set("")
    sv3.set("")
    sv4.set("")

    sv5.set("")  # 5~8python输出值
    sv6.set("")
    sv7.set("")
    sv8.set("")

def test_all():
    flag = np.zeros(8, dtype=float)
    error = np.zeros(8, dtype=float)
    error[0], flag[0] = eng.Test_sin_se(nargout=2)
    error[1], flag[1] = eng.Test_cos_se(nargout=2)
    error[2], flag[2] = eng.Test_tan_se(nargout=2)
    error[3], flag[3] = eng.Test_cot_se(nargout=2)

    flag[4], error[4] = test_sin()
    flag[5], error[5] = test_cos()
    flag[6], error[6] = test_tan()
    flag[7], error[7] = test_cot()

    dict_var = dict({0:sv1,1:sv2,2:sv3,3:sv4,4:sv5,
                     5:sv6,6:sv7,7:sv8})
    for i in range (8):
        if flag[i]:
            dict_var[i].set("AvgError: "+str('%.5f'%error[i]))
        else:
            dict_var[i].set("pass!")

bt3=Button(root,text='清除',font=('KaiTi',12,'bold'),width=5,height=2,command=clear_all)
bt3.grid(row=15,column=0,sticky = 'e' )

bt4=Button(root,text='测试',font=('KaiTi',12,'bold'),width=5,height=2,command=test_all)
bt4.grid(row=15,column=1,sticky = 'e' )


root.mainloop()
