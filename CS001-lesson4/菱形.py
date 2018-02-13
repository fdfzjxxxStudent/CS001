#triangle.py
print("Please input a number(1-9):")
n = int(input())            #三角形的高度为n行
for i in range(n+1):          #循环3遍，i从0到2
    s = '*' * (2*i+1)       #本行有2i+1个星号
    print(s.center(2*n+1))  #居中显示，总宽度为2n-1
for i in range(n):
    s = '*' * (2*n-2*i-1)
    print('',s.center(2*n))
