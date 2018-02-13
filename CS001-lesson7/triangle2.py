#triangle2.py
n=int(input())                   #三角形的高度为n行
for i in range(n-1,0,-1):          #循环n遍，i从0到n
    s = '*' * (2*i+1)       #本行有2i+1个星号
    print('%*s'%(n+i,s))    #输出字符串,宽度为n+i

for i in range(n):          #循环n遍，i从0到n
    s = '*' * (2*i+1)       #本行有2i+1个星号
    print('%*s'%(n+i,s))    #输出字符串,宽度为n+i
