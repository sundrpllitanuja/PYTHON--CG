#Loops
#for,while,break,range,continue,pass

#for()--sequence iterations

'''a=[10,20,30,40,50]
print(a)'''
#here i is temporary variable wher the data is seen
'''a=[10,20,30,40,50] 
for i in a:
    print(i)'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=",")''' #to print in single line


'''a=[100,200,300,400,500]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=(100,200,300,400,500)
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a={100,200,300,400,500}
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a={"name":"ram","city":"vjw","year":2026}
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={"name":"ram","city":"vjw","year":2026}
for i in a.keys():
    print(i)
    print(type(a))
    print(type(i))'''

'''a={"name":"ram","city":"vjw","year":2026}
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))'''

'''a={"name":"ram","city":"vjw","year":2026}
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[2.3,4.5,6.7]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=["dsa","c","java"]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[2+3j,7+2j]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[True,False]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[3,2.5,"tanu",1+2j,True,False]
print(a)
print(type(a))'''

#we use for because in situation like this like the above it shows as list but when we use for  very datatype is said
'''a=[3,2.5,"tanu",1+2j,True,False]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

#Task--
'''a=["vjw","hyd","vzg"]

for i in a:
    print(i.upper(),end=",")
    
b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#while()--continous iterations

'''a=10
while a>1:
    print(a)'''

'''a=10
while a>1:
    print(a)
    a=a-1'''
'''a=10
while a>=1:
    print(a)
    a=a-1'''
'''a=15
while a>1:
    print(a)
    a+=1'''
'''a=19
while a>1:
    print(a)
    a-=1'''      
    
'''a=5
while a<19:
    print(a)
    a+=1'''

#Task--
'''while True:
    cand1=int(input("enter the age"))
    if cand1>=18:
        print("eligible")
    else:
        print("not eligible")'''
#
'''while True:
    name=str(input("enter name"))
    if name=="Tanuja":
        print("Welcome Tanuja")
    else:
        print("welcome guest")'''
#
'''while True:
    price=int(input("enter price"))
    if price==1200:
        print("red velvet ")
    elif price==100:
        print("choco almond")
    elif price==800:
        print("choco")
    elif price==600:
        print("butterscotch")
    else:
        print("cake is not available")'''

#
'''while True:
    snack=str(input("enter snack"))
    if snack=="BBQ pizza":
        print(800)
    elif snack=="crispy chicken pizza":
        print(600)
    elif snack=="panner pizza":
        print(400)
    elif snack=="fries&coke":
        print(200)'''

#another Task-- attendance tracker(if,else)
'''students=5
s1=input("std1")
s2=input("std2")
s3=input("std3")
s4=input("std4")
s5=input("std5")
present=0
absent=0

if s1=="p":
    present+=1
else:
    absent+=1

if s2=="p":
    present+=1
else:
    absent+=1

if s3=="p":
    present+=1
else:
    absent+=1
    
if s4=="p":
    present+=1
else:
    absent+=1

if s5=="p":
    present+=1
else:
    absent+=1
    
print("Total",students)
print("Present",present)
print("Absent",absent)'''


# using loops
'''students=int(input("enter the total no.of students"))
a=0
p=0
for i in range(1,students+1):
    c=input(f"student{i} p/a")
    if c=="p":
        p+=1
    elif c=="a":
        a+=1
print("attendance tracker...........")
print("total students",students)
print("Present",p)
print("Absent",a)'''

#Range
# the range func return a sequence of numbers, starting from 0 by default and increments by 1 by 1 and stops before a specified number
#start-stop-step
#start
'''for i in range(10):
    print(i)'''
'''for i in range(10):
    print(i,end=" ")'''
#start- stop
'''for i in range(5,10):
    print(i)'''

#start-stop---step(inc)
'''for i in range(0,20,2):
    print(i,end=" ")'''

'''for i in range(0,50,5):
    print(i,end=" ")'''

'''for i in range(0,30,3):
    print(i,end=" ")'''

#TASK----
'''while True:
    i=int(input("enter marks"))
    if i in range(91,101):
        print(i,"Grade A")
    elif i in range(81,91):
        print(i,"Grade B")
    elif i in range(71,81):
        print(i,"Grade C")
    elif i in range(51,71):
        print(i,"Grade D")
    elif i in range(0,51):
        print(i,"Fail")'''
        
#diff break,continue and pass----these work only in for and while loops
        
#break-- it is used to terminate the entire loop
#continue-- it is used to skip the current iteration and rest of code will continue
#pass-- it is a null statement, it does nothing but syntatically we need

#break
'''a=10
while a>1:
    print(a)
    a=a-1'''
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''
'''a=20
while a>1:
    a=a-1
    if a==6:
        break
    print(a)'''

'''for i in range(25):
    if i==15:
        break
    print(i)'''

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#cont---
'''a=30
while a>10:
    a=a-1
    if a==26:
        continue
    print(a)'''

'''a="python"
for i in a:
    if i=="h":
       continue
    print(i)'''
#pass

'''for i in range(25):
    if i==15:
       pass
    print(i)'''

a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        pass
    
    
        




    






