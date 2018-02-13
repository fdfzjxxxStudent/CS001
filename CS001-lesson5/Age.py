#Age.py
import time
def age(birth_year):
    this_year=time.localtime().tm_year  #得到当前的年份，赋值给this_year
    return this_year-birth_year         #返回今年和出生年份之差，即年龄

year=int(input('Which year were you born?'))    #读取用户键入的出生年份
Age=age(year)                           #把它作为参数，传给age函数得到年龄
print('You are',Age,'years old.')
