#Homework_3_3.py
print("Please input the distance(km):")
distance = float(input())
print("Please input the waiting time(minute):")
wait_time = float(input())
fee = 0

if distance < 0 or wait_time < 0:
    print('Wrong number!')
    exit()

if distance <= 3:
    fee = 14
elif distance <= 15:
    fee = 14 + (distance-3) * 2.5
else:
    fee = 14 + 12 * 2.5 + (distance-15) * 3.6

fee = fee + (wait_time//4) * 2.5
if wait_time % 4 != 0:
    fee = fee + 2.5

print('You should pay', fee, 'RMB.')
