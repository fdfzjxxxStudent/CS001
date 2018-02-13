#draw1.py
#从turtle导入所有函数
from turtle import *
#定义绘图的速度，数值越大，速度越快
speed(5)
color("purple")     #定义绘制时画笔的颜色
#注意：画笔初始位置在画布中央，即坐标原点(0,0)。方向水平向右。

for i in range(3):  #重复三次
    forward(200)    #前进200像素
    right(120)      #右转120度
    
up()                #抬起画笔
goto(0, 50)         #移动至坐标(0,50)
down()              #落笔

color("red")
for i in range(4):  #重复四次
    forward(200)    #前进200像素
    left(90)        #左转90度

color("white")
