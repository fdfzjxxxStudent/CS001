#string1.py
s = 'Tom studied in MIT. It\'s a famous university in USA.'
for c in s:
    if c.islower():
        print(c, end='')
