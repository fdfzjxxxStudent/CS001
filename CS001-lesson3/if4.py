#if4.py
score = int(input('Please input the score:'))
if score >= 80:
    if score >= 90:
        print('Excellent!')
    else:
        print('Good!')
else:
    if score >= 60:
        print('Pass!')
    else:
        print('Fail!')
