#file2.py
#定义函数，用于把形参fname所指定的的内容打印到屏幕上
def readandprint(fname):
    f = open(fname,'r+')
    while True:
        line = f.readline() #读取一行字符到line，包括行尾的换行符\n
        if line == '':      #如果没读到东西，说明已到文件末尾
            print("读取完成！按Enter退出")
            input()
            exit()
            break           #退出死循环
        print(line.strip()) #否则，打印这行。思考：为什么要使用strip?
    f.close()
fname = input("请输入文件名以及扩展名（如在不同文件夹下，请输入文件路径）：")
readandprint(fname)  #调用函数，指定实参为sample.txt
