#Function2.py
import time
def introduce(name,age):
    print("I'm",name+'.')
    print("I'm",age,"years old.")

this_year=time.localtime().tm_year
age = this_year-2006   
introduce("XiyuWang",age)
print(" ")

print("---------------Input Area---------------")
name = input("Now,please input your name:")
age = int(input("When did you born?"))
print("----------------------------------------")
this_year=time.localtime().tm_year
age = this_year-age
error = age-time.localtime().tm_year
if error>=0:
    print("")
    print("Error:You hadn't been born!")
    time.sleep(3)
    exit()
if error==0:
    print("")
    print("Error:You are 0 years old?That's impossible!You can't control the computer if you are so that small!")
    exit()
if age==str():
    print("")
    print("Error:You can only input a number!")
    time.sleep(3)
    exit()
else:
    print("")
    introduce(name,age)
