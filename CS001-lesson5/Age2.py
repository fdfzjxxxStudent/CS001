#Age2.py
import time
def age(birth_year):
    this_year=time.localtime().tm_year
    return this_year-birth_year

year=int(input('Which year were you born?'))
print('You are',age(year),'years old.') #函数返回的结果直接用做print的输出项
