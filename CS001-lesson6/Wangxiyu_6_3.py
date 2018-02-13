#HighestMark
mark = 0
highestnumber = 1
lista = []
listb = []
while True:
    print("Enter a number(-1 indicats end):")
    mark = float(input())
    lista.append(mark)
    if mark == -1:
        break
    print("Enter name:")
    name = input()
    listb.append(name)
M = max(lista)
print("Who got the highest score:")
for i in range(len(lista)):
     if lista[i] == M:
        print(listb[i])
