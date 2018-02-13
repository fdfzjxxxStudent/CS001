#Homework_3_2.py
print("How many stations did you take?")
n = int(input())
if n <= 0:
    print('Wrong number!')
elif n <= 5:    
    print('You should pay 3 RMB.')
elif n <= 9:
    print('You should pay 4 RMB.')
elif n <= 12:
    print('You should pay 5 RMB.')
else:
    print('You should pay 6 RMB.')
