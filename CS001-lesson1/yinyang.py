#yinyang.py
#绘制太极阴阳鱼
from turtle import *
speed(10)
width(3)                    #设置画笔宽度
radius=200                  #设置半径为200

#绘制黑色鱼形
color("black", "black")     #设置画笔颜色为黑色，填充颜色为黑色
begin_fill()                #开始填充（如果形成封闭形状，内部填充）
circle(radius/2, 180)       #逆时针绘制半径减半的半个圆形（180度）
circle(radius, 180)         #绘制外缘半个圆形
left(180)                   #180度调头
circle(-radius/2, 180)      #顺时针绘制半径减半的半个圆形
end_fill()                  #结束填充

#画笔移到新位置
left(90)                    #左转90度
up()                        #抬起画笔
forward(radius*0.35)        #画笔前进一段距离
right(90)                   #右转90度
down()                      #画笔落下

#绘制白色小圆圈
color("black", "white")     #设置画笔颜色为黑色，填充颜色为白色
begin_fill()
circle(radius*0.15)         #绘制完整圆形
end_fill()

#画笔退回初始位置（画布中心）
left(90)
up()
backward(radius*0.35)
down()
left(90)

#绘制白色鱼形

#画笔移到新位置

#绘制黑色小圆圈

