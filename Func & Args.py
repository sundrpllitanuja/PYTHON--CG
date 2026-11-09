# FUNCTION-Arguments----
#1) function is a block of organized,reusable code and that is used to perform a single or multiple tasks
#2) python gives in built func like print or u can make ur own functions and these are called user defined func
#3) func block begins with a def follwed by a func name and paranthesis(())---a,b are arguments 10,20 are parameters or positional arguments

'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

#func
'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

#pow **
#modulus %
#int division //

'''def cal(a,b):
    print("the pow is",a**b)
    print("the modulus is",a%b)
    print("the intdiv is",a//b)
cal(2,5)
cal(10,2)'''

'''def add(a,b):
    c=a+b
    print(c)
add(7,8)'''

'''def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()'''

#fullname
'''def fullname():
    fname=input("enter fname")
    lname=input("enter lname")
    print((fname+" "+lname).title())
fullname()'''

#diff b/w print and return
#print just shows human user o/p in a console
#return is used to terminate the func gives back value from a func

'''def sub(a,b):
    print(a-b)
sub(4,8)'''

'''def sub(a,b):
    return a-b
sub(4,8)'''# no o/p is shown we need print to show


'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(5,2)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e #we need to give in 1 line

print(cal(5,2))'''



##TASK----
'''while True:
    def cal():
        a=int(input("enter a value"))
        b=int(input("enter b value"))
        option=int(input("choose:\n1.Add\n2.Sub\n3.Mul"))
        if option==1:
            print(a+b)
        elif option==2:
            print(a-b)
        elif option==3:
            print(a*b)
        else:
            print("Invalid Option")
    cal()'''
#another method
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    option=int(input("choose:\n1.Add\n2.Sub\n3.Mul"))
    if option==1:
        add()
    elif option==2:
        sub()
    elif mul():
        mul()
    else:
        print("Invalid Option")'''

#12/10/2026--Arguments

#keyword and Positional Arguments-----
#1
'''def details(id,name,mailid):
    id=10
    name="tanuja"
    mailid="tanu@gmail.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")'''

#2
'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id=20,name="ram",mailid="ram@gmail.com")
details(id=30,name="rani",mailid="r@gamil.com")
details("sai","s@gmail.com",40)  #arg are must so that the doesnt mismatch
details(name="liya",mailid="liya@gmail.com",id=50)'''

#TASK---

'''def details(id,name,mailid,salary,dsg):
    print(id,name,mailid,salary,dsg)
    
details(id="id",name="name",mailid="mailid",salary="salary",dsg="dsg")
details(id=20,name="ram",mailid="ram@gmail.com",salary=200000,dsg="HR")
details(id=30,name="rani",mailid="r@gamil.com",salary=150000,dsg="ASS-HR")
details(name="liya",mailid="liya@gmail.com",id=40,salary=20000,dsg="sales")
details(id=50,name="nila",mailid="nila@gmail.com",salary=20000,dsg="sales")
details(id=60,name="eswar",mailid="es@gmail.com",salary=20000,dsg="sales")
details(id=70,name="ciya",mailid="ciya@gmail.com",salary=20000,dsg="sales")
details(id=80,name="ramrao",mailid="rr@gmail.com",salary=20000,dsg="sales")'''

#Default Arg---
#1
'''def grcy(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grcy("rice",2000)'''

#2
'''def grcy(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
grcy("dal")'''

'''def grcy(item="ghee",price):--#error
#non-default arg followa default arg
    print("item is %s" %item)
    print("price is %.2f" %price)
grcy(2000)'''


'''def grcy(item="salt",price,qty):----#error
    print("item is %s" %item)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
grcy(20,2)'''

#TASK-----
'''def bakery(cake,price,qty):
    print("cake is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %s" %qty)
    
bakery("choco",2000,"1kg")
bakery("straw berry",2500,"1kg")
bakery("choco chip",2300,"1kg")
bakery("butterscotch",1800,"1kg")
bakery("kaju",3000,"1kg")'''

#TASK___split bill
#1
'''def sp_bill():
    persons=int(input("enter persons"))
    amt=int(input("enter amount"))
    bill=amt/persons
    
    print("N0.of Persons-%d" %persons)
    print("Amount is %.2f" %amt)
    print("Per Head is %d" %bill)
sp_bill()'''

#2
'''def sp_bill():
    a=int(input("enter persons"))
    b=int(input("enter amount"))
    print(f"per head bill is{b//a}")
    print("per head bill is{}".format(b//a))
sp_bill()'''

#3
'''def sp_bill():
    a=int(input("enter persons"))
    b=int(input("enter amount"))
    c=b//a
    print(f"per head bill is{c}")
    print("per head bill is{}".format(c))
sp_bill()'''

    



#15/10/2026
# *-arguments--used to unpack elements

'''a=[1,2,3,4,5,6,7]
print(a)
print(*a)'''

'''a=(1,2,3,4,5,6,7)
print(a)
print(*a)'''

'''a={1,2,3,4,5,6,7}
print(a)
print(*a)'''

'''a={"year":2026,"month":10}
print(a)
print(*a)'''

'''a,b,c=3,4,5,6,7,8,9,10--#error
print(a)
print(b)
print(c)'''

'''a,*b,c=3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)'''

'''a,*b,c=3,4,5,6,7,8,9,10
print(a)
print(*b)
print(c)'''

'''a,b,*c=3,4,5,6,7,8,9,10
print(a)
print(b)
print(*c)'''

'''a,b,c="codegnan"--#error
print(a)
print(*a)'''

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,*b,c="codegnan"
print(a)
print(*b)
print(c)'''

#var-length Arguments-this automatically stores in tuple and we use star(*) argument
'''def check(*a):
    print(a)
    print(type(a))
check()
b=[2,3,4,5,6]
check(*b)
c=(7,8,9,12,13)
check(*c)
d={2,3,4,5,6,7}
check(*d)
e={"city":"vja"}
check(*e)'''

#TASK
'''def check1(*a):
    d=2#creating temporary variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,1.2,4.5)
check1(1,2,3.4,4.5,"pooja")'''


#Task====
'''while True:
    def railway_ticket():
        ticket=1000
        gender=input("enter gender")
        age=int(input("enter age"))
        if gender=="m":
                if age>=60:
                   print("senoior citizen")
                   ticket=ticket-30/100*ticket
                   print(ticket)
                elif age<60:
                    print("normal citizen")
                    print(ticket)
        elif gender=="f":
             if age>=60:
                print("senoior citizen")
                ticket=ticket-50/100*ticket
                print(ticket)
             elif age<60:
                    print("normal citizen")
                    print(ticket)

    railway_ticket()'''


#16/10/2026--
#Kwargs(**)-----
'''def check(**a):
    print(a)
    print(type(a))
check()
details={"id":[1,2,3],
         "name":["ram","sai","riya"],
         "status":["p","a","p"]}
check(**details)'''

'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)

check()
details={"id":[1,2,3],
         "name":["ram","sai","riya"],
         "status":["p","a","p"]}
check(**details)'''

#using * & **
'''def check1(*a,**b):
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
    

check1()
data=(2,3,4,5,4.5,6.7)
check1(*data)
              
details={"id":[1,2,3],
         "name":["ram","sai","riya"],
         "status":["p","a","p"]}
check1(**details)
check1(*data,**details)'''


#ASCII--
#chr()--numerics pass
'''print(chr(90))
print(chr(65))
print(chr(91))

#ord()--alp pass
print(ord("a"))
print(ord("z"))'''

#TASK---

'''for i in range(65,91):
    print(chr(i),end=" ")

for i in range(97,123):
    print(chr(i),end=" ")'''

#TasK--
a=str(input("enter name"))
for i in a:
    print(ord(a[i]))
    



                    
        
    


























                
        
        
        
                

    
            

    







