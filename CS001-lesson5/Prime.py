#Prime.py
def IsPrime(n):
    for j in range(2,n):
        if i%j!=0:
            return True

for i in range(2,100):      #i从2循环到99
    if IsPrime(i):          #如果函数返回True，即i是质数
        print(i)            #输出i
