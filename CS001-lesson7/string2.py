#string2.py
list = []
s = input()
for c in s:
    if c.isdigit() or c.isalpha():
        list.append(c)
n=int(''.join(list))
print(n)
        
