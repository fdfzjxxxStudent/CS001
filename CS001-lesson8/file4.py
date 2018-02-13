#file4.py
#定义函数，用于从文件对象f中读取一行的5项信息，
#并打印出来，每行一项信息
def readOneLine(f):
    no=f.read(8)        #读取8个字符(编号及后面的空格）
    engname=f.read(8)   #读取8个字符(英文名字及后面的空格）
    chnname=f.read(12)  #读取12个字符(中文名字的4个汉字及后面的8个空格）
    city=f.read(12)     #读取12个字符(城市的4个汉字及后面的8个空格）
    postcode=f.read(7)  #读取7个字符(邮编字的6位数字及后面的换行符\n）
    print(no)
    print(engname)
    print(chnname)
    print(city)
    print(postcode)
f=open('university.txt')#思考：如果改为sample.txt，为什么会不成功？
readOneLine(f)  
readOneLine(f)  
f.close()
