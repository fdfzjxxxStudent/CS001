#Average3.py
count = 0
sum = 0
while True:         #死循环
    score = float(input('Please input a score(-1 indicates end):'))#读取一个成绩
    if score == -1: #如果读到-1
        break       #退出死循环
    sum += score    #累加总分
    count += 1      #计数加一
print('You input', count, 'scores.')
if count != 0:
    print('The average is', sum/count)
      
