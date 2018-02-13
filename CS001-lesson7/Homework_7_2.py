#Homework_7_2.py
s = input()            
for c in s:                         #c代表s中的每个字符
    if c.isupper():                 #如果c是大写字母
        print(c.lower(), end='')    #输出其对应的小写
    elif c.islower():               #如果c是小写字母
        print(c.upper(), end='')    #输出其对应的大写
    else:                           #其它字符
        print(c, end ='')           #原样输出
