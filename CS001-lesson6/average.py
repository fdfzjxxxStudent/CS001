#average.py
scores=[90,89,95,100,85]
sum=0
n=0
for s in scores:
    sum+=s
    n+=1
print('Average:%.2f'%(sum/n))
