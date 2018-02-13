#NameReplace
print("---------Enter five names---------")
a = input('1.')
b = input('2.')
c = input('3.')
d = input('4.')
e = input('5.')
namelist = [a,b,c,d,e]
print("")
print("---------Replace one Name---------")
newnumber = int(input("Replace one name. Which one?(1-5):"))
if newnumber > 0 and newnumber <6:
    new = str(input("New name:"))
    namelist[newnumber-1] = new
else:
    print(newnumber,"is wrong position!")
    exit()
print("")
print("-----------Replaced Name-----------")
print('1.',namelist[0],sep='')
print('2.',namelist[1],sep=')
print('3.',namelist[2],sep=')
print('4.',namelist[3],sep=')
print('5.',namelist[4],sep=')
print("-----------------------------------")
input()
