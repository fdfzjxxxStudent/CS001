#Homework_7_3.py
s = input()            
list = s.split(' ')
Sum = 0
n = 0
for i in list:
    Sum += float(i)
    n += 1
print('%.2f' % (Sum/n))
