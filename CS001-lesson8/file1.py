#file1.py
f=open('sample.txt','w')    #写模式打开或创建sample.txt文件
s1='1\tfudan\t复旦大学\t中国上海\t200433\n' 
s2='2\tsjtu\t交通大学\t中国上海\t200240\n' 
f.write(s1)                 #向文件中写入字符串s1
f.write(s2)                 #向文件中写入字符串s2
f.close()
print("写入成功！文件名：sample.txt")
