#Average2.py
count = 0           #计数器初始为0
sum = 0             #总分初始为0
score = float(input('Please input a score(-1 indicates end):'))#读取一个成绩
while score != -1:  #如果读到的不是-1，进入循环；如果是-1，离开循环
    sum += score    #把成绩累加到总分上
    count += 1      #计数器加一
    score = float(input('Please input a score(-1 indicates end):'))#读下一个成绩
print('You input', count, 'scores.')    #输出一共多少个成绩
if count!=0:                            #如果不是0个成绩
    print('The average is',sum/count)   #输出平均分
      
