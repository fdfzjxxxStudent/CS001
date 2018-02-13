#Highest.py
s = '80 Tom 90 Mike 85 Sam 90 Dora'
list = s.split(' ')     #按空格把字符串拆成列表
scores = list[::2]      #从0开始切片,步长2,得到成绩列表
names = list[1::2]      #从0开始切片,步长2,得到成绩列表
maxscore = max(scores)  
print('Who got the highest score:')
for i in range(len(scores)):
    if scores[i] == maxscore:
        print(names[i])

