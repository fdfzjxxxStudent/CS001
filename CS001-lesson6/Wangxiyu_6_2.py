#NameReplace
print("Enter 5 names:")
a = input()
b = input()
c = input()
d = input()
e = input()
namelist = [a,b,c,d,e]
print("The names are:")
print(a)
print(b)
print(c)
print(d)
print(e)
print("Replace one name. Which one?(1-5):")
newnumber = int(input())
if newnumber > 0 and newnumber <6:
    print("New name:")
    new = str(input())
    namelist[newnumber-1] = new
else:
    print(newnumber,"is wrong position!")
    exit()
print("The names are:")
namelist[newnumber-1] = new
print(namelist[0])
print(namelist[1])
print(namelist[2])
print(namelist[3])
print(namelist[4])
