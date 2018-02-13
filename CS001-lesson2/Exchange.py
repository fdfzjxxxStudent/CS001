#Exchange.py
rate = 6.78                             #1美元兑换多少人民币
dollar = float(input("Dollars:$"))      #请用户键入欲兑换的美元数量，转换为浮点数
rmb = dollar * rate                     #计算兑换的人民币数量
print('RMB:￥%.2f' % rmb, sep='')       #输出小数点后2位
