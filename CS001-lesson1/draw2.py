#draw2.py
#从turtle导入所有函数
from turtle import *
#定义绘图的速度，数值越大，速度越快
speed(100000000)
color("purple")     #定义绘制时画笔的颜色
#注意：画笔初始位置在画布中央，即坐标原点(0,0)。方向水平向右。

for i in range(120):#重复120次
    forward(200)    #前进200像素
    right(121)      #右转121度
    
