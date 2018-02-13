#Times2.py
for i in range(1, 10):           #外层循环，循环变量i从1到3，输出3行
    for j in range(1,11-i):     #内层循环，当第i行时，j从1到i
        print(i, '*', j, '=', i*j, '\t', end='')#输出此时的i和j的乘积
    print()                     #本行结束，输出换行
