#file3.py
f = open('sample.txt')  
lines=f.readlines()     #读取文件各行内容，返回列表
#print(lines)           #可以去掉这一行最前面的#，打印列表的内容看一下
for line in lines:      #对列表中的每个元素，即每行字符
    print(line.strip()) #打印出来
f.close()
