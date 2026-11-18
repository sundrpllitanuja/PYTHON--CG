#OOPS-- object oriented language system/structure language
        #1 a class contains attributes,variablesand methods or functions that can manipulate the data
        #2 a class is the blueprint of an object
        #3 a object is an intiation of a class
        #4 methods are func defined inside the body of the class

#--4 Pillars of OOPS-
                   
                  #1.Polymorphism---#operator over-loading
                                    #operator over-riding
                                    #method over-loading
                                    #method over-riding
                  
                  #2.Inheritance----#single
                                    #multiple
                                    #multi-level
                                    #hybrid
                                    #hirechical
                                    #super func
                
                 #3.Encapsulation---#public__
                                    #protected_
                                    #private
                 
                #4.Abstraction---#abstract class
                                 #abstract method

#syntax
'''class classname():  #class
    #attributes
    name="tanu"
    age=20
    place="vja"
    def funcname(method_name):
        print("statements")
a=classname() #object
print(dir(a))
a.fname()'''


#class declaration
'''class details():
    name="tanu"
    age=20
    place="blr"
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''

#object instantiation
'''class details():
    def data (self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details()
b=details()
print(dir(a))
a.data("sai",22,"blr")
b.data("rani",24,"vja")
a.display()
b.display()'''


#object intialization
'''class details():
    #creating constructor
    def __init__(self,name,place,age):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details("sai",22,"blr")
print(dir(a))
a.display()'''

#with constructor
'''class details():
    #creating constructor
    def __init__(self,name,place,age):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)

a=details(name=input("enter name"),
        age=int(input("enter age")),
        place=input("enter place"))
print(dir(a))
a.display()'''


'''class details():
    def __init__(self):
        self.a=input("enter name")
        self.b=int(input("enter age"))
        self.c=input("enter place")
        
    def display(self):
        print(self.a,self.b,self.c)
a=details()
print(dir(a))
a.display()'''

#diff b/w _&__
#when user wants to create a variable with __ our python interpreter treats it as a special variablet to avoid name conflicts with methods and inner classes

'''class Employee():
    def __init__(self):
        self.name="tanuja"
        self._mailid="tanu1@gmail.com"
        self.__salary=10000 #private variable
class Employee1():
    def __init__(self):
        self.name="sai"
        self._mailid="sai1@gmail.com"
        self.__salary=20000
    

a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)--error 
print(a._Employee__salary)

a=Employee1()
print(a.name)
print(a._mailid)
print(a._Employee1__salary)'''

##_____Polymorphism_____
#operator over-loading 
'''a=2;b=5
print(a+b)
print(a.__add__(b))
print(a.__add__(10))
print(a.__sub__(b))
print(a.__mul__(3))
#print(a.__div__(10))
print(a.__pow__(2))
print(a.__le__(1))
print(a.__ge__(0))

a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(2))

a="code";b="gnan"
print(a+b)

a="python";b="course"
print(a.__add__(" "+b).title())
print("pooja".__add__(" "+"s").title())'''

#operator over-riding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(10)
y=B(5)
print(x+y)'''

#method over-loading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("program endss..")

x=new()
x.sum()
x.sum(2,3,4)
x.sum(6,4)'''

'''class new():
    def sum(self,a=10,b=20,c=30):
        if a!=1 and b!=2 and c!=3:
            print("the sum is",a+b+c)
        elif a!=10 and b!=20:
            print("the product is",a*b)
        else:
            print("program endss..")

x=new()
x.sum()
x.sum(12,10,4)
x.sum(1,2)'''


#method over-riding--same functin differrent behaviour
'''class Animal():
    def speak(self):
        print("animal can make sounds")
class dog():
    def speak(self):
        print("dog can bark")
a=Animal()
b=dog()
a.speak()
b.speak()'''

'''class Car():
    def Vehicle(self):
        print("car has motor")

class Bike():
    def Vehicle(self):
        print("bike has motor")

a=Car()
b=Bike()
a.Vehicle()
b.Vehicle()'''

#Inheritance
#single---
'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        print("available cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
    cash=50000
    def new_cash(self):
        print("new cash is",self.cash+self.cash)
        print("new cash is",RBI.cash+self.cash)

a=HDFC()
a.available_cash()
a.new_cash()'''


#multiple--
'''class father():
    height=6
    def father_height(cls):
        print("father height is ",cls.height)

class mother():
    weight=60
    def mother_weight(cls):
        print("mother weight is",cls.weight)
        
class child(father,mother):
    dob="11-11-2026"
    def child_dob(cls):
        print(" Child dob is",cls.dob)
a=child()
a.child_dob()'''



'''class father():
    height=6
    def father_height(cls):
        print("father height is ",cls.height)

class mother():
    weight=60
    def mother_weight(cls):
        print("mother weight is",cls.weight)
        
class child(father,mother):
    dob="11-11-2026"
    def child_dob(cls):
        print(" Child dob is",cls.dob)
a=father()
b=mother()
c=child()
a.father_height()
b.mother_weight()
c.child_dob()'''


#multi-level
'''class Grandfather():
    def gf_land(cls):
        print("land is 6 acres ")

class father(Grandfather):
    def house_ft(cls):
        print("100sqft")
        
class child(father):
    def child_car(cls):
        print("ev")

a=child()
a.gf_land()
a.house_ft()
a.child_car()'''


#hierarchical--this means 1 parent class is inherited by multiple child classes
#task
#employee--cmp name parent
#trainer-teaching sub child1
#developer-code       child2

'''class employee():
    def comp_name(cls):
        print("codegnan")

class trainer(employee):
    def teaching(cls):
        print("python")
        
class developer(employee):
    def code(cls):
        print("coder")

a=trainer()
b=developer()
a.teaching()
b.code()'''

#Hybrid--it means combination of both hirearchical and multiple inheritance
'''class person():
    def details(cls):
        print("Tanuja")

class student(person):
    def learn(cls):
        print("python")

class trainer(person):
    def teach(cls):
        print("coding")

class prg_manager(student,trainer):
    def manager(cls):
        print("manage both student and trainer")

a=prg_manager()
a.details()
a.manager()
a.teach()
a.learn()'''

#super function---(bulit-in)
'''class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def __init__(self,name,age):
        super(). __init__(name)
        self.age=age
        print("child constructor")

obj=child("tanu",20)
print(obj.name)
print(obj.age)'''


#Encapsulation--we can combine multiple units into single unit is known as encapsulation
#publicdata
'''class A():
    publicdata=10
    def method1(self):
        print(self.publicdata)
class B(A):
    def method2(self):
        print(self.publicdata)

obj=B()
obj.method1()
obj.method2()'''


#_protected data
class A():
    _protecteddata="100"
    def method1(self):
        print(self._protecteddata)

class B(A):
    def method2(self):
        print(self._protecteddata)
obj=B()
obj.method1()
obj.method2()
print(obj._protecteddata)


#__private data
class A():
    __privatedata="tanuja"
    def method1(self):
        print(self.__privatedata)
class B(A):
    def method2(self):
        print(self._A__privatedata)
obj=B()
obj.method1()
obj.method2()

#Abstraction-hiding unnecessary info from user is called abstraction
#abstarct class--1/more abstract methods is called abstract class
#abstarct method-- a method is declared without implementation is called abstartct method

'''class A():
    def method1(self):
        pass
obj=A()
obj.method1()'''

class A():
    def method1(self):
        print("data")
obj=A()
obj.method1()

'''from abc import ABC,abstarctmethod
class A():
    def method1(self):
        print("hello there")
obj=A()
obj.method1()'''  #error

#######
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("welcome")
    @abstractmethod
    def method3(self):
        pass

class B(A):
    def method1 (self):
        print("method1 implemented")
    def method3(self):
        print("method3 implemented")

obj=B()
obj.method1()
obj.method2()
obj.method3()









        
    





                            
                    
