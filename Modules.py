#_______MODULES________
#difference b/w Module,Library and Package:

#Module---- 1.a module is a single python file,it consists python code
           #2.it contains functions,variables and classes
           #3.ex--math.py,random.py and mymodule.py
                                            
#Package--- 1.a package contains 1/more python modules/files
           #2.numpy,pandas,and requests

#Library---1.a library can consists of both modules and library
          #2.ex--numpy,pandas,django,matplotlib

###NOTE--every python file is module and import is a keyword and
       # every python file is saved internally with variable name as (__main__)

'''def greetings(name):
    print("welcome",name)'''

'''a=4
b=7
print(a+b)'''

'''a=int(input("enter"))
b=int(input("enter"))
print(a+b)'''


'''if __name__=="__main__":
    a=[10,20,30,40,50]
    a.append("code")
    a.extend("code")
    print(a)'''

'''def dummy():
    if __name__=="__main__":
        print("this program is run as script") # else it is script
    else:
        print("this program is run as module") # only if import is used
dummy()'''

#####-----Math Module----
'''import math
print(math.pi)
print(math.pi*3)
print(math.log(10))
print(math.sin(30))
print(math.cos(60))
print(math.tan(45))
print(math.sqrt(2))
print(math.pow(2,5))
print(math.ceil(2.9))
print(math.floor(4.4))'''


'''from math import pi,sqrt,log
print(pi,sqrt(2),log(20))'''


####------System Module----
'''import sys
print(sys.path)#this prints in list

for i in sys.path:  #this prints line by line
    print(i)

print(sys.version)'''

####------OS Module----
'''import os
print(os.path)
print(os.getcwd) #get current working directory
print(os.listdir)
print(os.mkdir("oct30"))
print(os.listdir())'''

####-----Random Module----
        #to generate random numbers in python,randint() func is used this func is defined in random module
#sample()--prints what range we have given (5)ex
'''import random
a=random.sample(range(20,40),5)
print(a)'''

#randint()--prints single number only
'''a=random.randint(20,40)
print(a)'''

#choice()--prints from the given list only
'''a=[1,2,3,4,5,6]
b=random.choice(a)
print(b)'''

#TASK--Dice
'''while True:
    import random
    a=int(input("enter the roll of dice"))
    b=random.randint(1,6)
    print(b)
    option=int(input("choose:\n1.YES\n2.NO"))
    if option==1:
        pass/continue
    else:
        break'''



#####-----Calendar Module----
'''import calendar
year=2027
month=11
print(calendar.month(year,month))''' #year lo only 1month

'''import calendar
year=2027
print(calendar.calendar(year))'''#whole year

#TASK-
'''import calendar
a=int(input("Enter Year"))
b=int(input("Enter Month"))
print(calendar.month(a,b))'''

#Date and Time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

#epoch time
'''import time
a=time.time()
print(a)

b=time.localtime(a)
print(b)
print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")

print(f"time is {b.tm_hour}.{b.tm_min}.{b.tm_sec}")

print(f"Day is {b.tm_wday}--{b.tm_yday}--{b.tm_isdst}")'''

#_______Regular Expression____(regex)_____
#regular expression are powerful tools(modules) embedded in python which is mainly used to
#find a pattern within a given string or statements or files and we mainly use it for text manipulation 

'''a="codegnan is in vja"
print(a)'''

'''a="codegnan\nis\tin\nvja"
print(a)'''
#rstring--no change 
'''a=r"codegnan\nis\tin\nvja"
print(a)'''

#sequence characters--
'''
\w->it matches alpha-numeric
\W->it doesn't match alpha-numeric
\d->it matches any digit
\D->it doesn't matches any digit
\s->it represents white spaces
\S->it represents non-white spaces

'''

#compile(),search(),findall(),split(),sub()

#compile()
'''import re
a="map mat cat money cash code cap maths mug dog donkey"
b=re.compile(r"\w\w\w\w")
print(b)

#search()
c=b.search(a)
print(c)

d=re.search(r"m\w+",a)
print(d)'''

#findall()
'''e=re.findall(r"m\w+",a)
print(e)

f=re.findall("d\w+",a)
print(f)

g=re.findall("c\w+",a)
print(*g)'''  #*to unpack

#split()
'''b=re.split(r"m",a)
print(b)

b=re.split(r"\s",a)
print(b)

b=re.split(r"\S",a)
print(b)'''

#sub()
'''c=re.sub(r"maths","science",a)
print(c)'''

#digits
'''a="year 2026 month 10 date 23 day 4"
b=re.findall(r"\d+",a)
print(b)

a="year 2026 month 10 date 23 day 4"
b=re.findall(r"\D+",a)
print(b)'''




 







    
    
