#if3error.py
score = int(input('Please input the score:'))
if score >= 80:
    print('Good!')
elif score >= 90:
    print('Excellent!')
elif score >= 60:
    print('Pass!')
else:
    print('Fail!')
