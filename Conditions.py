#CONDITIONS--
#if using operators(comparision,logical,identity,membership)

#1----if
#if using comparsion- <,>,<=,>=,!=,==
'''a=10
b=15
if a<b:
    print("true")'''

'''a=19
b=80
if a>b:
    print("true")'''

'''a=10
b=15
if a<=b:
    print("true")'''

'''a=10
b=15
if a>=b:
    print("true")'''

'''a=10
b=15
if a!=b:
    print("true")'''

'''a=10
b=10
if a==b:
    print("equals")'''
#run_time--

'''a=int(input("enter a value"))
b=int(input("enter b value"))
if a<b:
    print("true")'''

'''a=int(input("enter a value"))
if a!=90:
    print("true")'''
#we can also give strings
'''a="python"
if a!="java":
    print("match")'''
a="python"
if a=="java":
    print("match")

#if using logical--and- must 2 cond be either true or false,or-if either one cond is true it gives output ,not
'''a=4
b=6
if a<b and a>b:
    print("true")'''

'''a=14
b=10
if a<=b and a>=b:
    print("true")'''

'''a=24
b=26
if a!=b and a==b:
    print("true")'''

#or
'''a=4
b=6
if a<b or a>b:
    print("true")'''

'''a=50
b=100
if a<=b or a>=b:
    print("true")'''

'''a=14
b=10
if a!=b or a==b:
    print("true")'''
'''a=14
b=10
if not a>b:
    print("true")'''

'''a=14
b=10
if not a<b and a>b:
    print("true")'''
#run_time--
'''a=int(input("enter"))
b=int(input("enter"))
if a>b:
    print("a is greater")'''

'''a=int(input("enter"))
b=int(input("enter"))
if a>b and b>a:
    print("a is greater")'''
'''a=int(input("enter"))
b=int(input("enter"))
if a>b or b>a:
    print("a is greater")'''

'''a=int(input("enter"))
b=int(input("enter"))
if not a<b:
    print("a is greater")'''
#if using identify-is, is not
'''a=5
if type(a) is int:
    print("integer")'''

'''a=5
if type(a) is not int:
    print("integer")'''
'''a=5
if type(a) is str:
    print("integer")'''

'''a="ai"
if type(a) is str:
    print("string")'''

#runtime--
'''a=int(input("enter"))
if type(a) is int:
    print("integer")'''

'''a=int(input("enter"))
if type(a) is not int:
    print("integer")'''

'''a=str(input("enter"))
if type(a) is str:
    print("string")'''

#if using membership--in ,notin

'''a=1,2,3,4,5,6,7,8,9
if 10 in a:
    print("true")'''

'''a=1,2,3,4,5,6,7,8,9
if 10 not in a:
    print("true")'''
#run_time--
'''a=int(input())
if 10 in a:
    print("true")''' #error canot gibe direct i/p

'''a=[1,2,3,4,5,6,7,8,9]
b=int(input("enter"))
if b in a:
    print("true")'''

#2----if-else
#if-else using comparision
'''a=10
b=20
if a<b:
    print("true")
else:
        print("false")'''

'''a=10
b=20
if a==b:
    print("true")
else:
        print("false")'''
'''a=10
b=20
if a!=b:
    print("true")
else:
        print("false")'''

#if else using logical--and ,or, not

'''a=10
b=20
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=100
b=200
if a<=b or b>=a:
    print("true")
else:
    print("false")'''


'''a=10
b=20
if not b>a:
    print("true")
else:
    print("false")'''

#if else using identity-is,isnot
'''a=10
if type(a)is int:
    print("true")
else:
    print("false")'''

'''a=10
if type(a)is not int:
    print("true")
else:
    print("false")'''

#if else using membership in ,not in
'''a=10,11,12,13,14,15
if 15 in a:
    print("true")
else:
    print("false")'''

'''a=10,11,12,13,14,15
if 155 not in a:
    print("true")
else:
    print("false")'''

#run_time
'''a=int(input("enter"))
b=int(input("enter"))
if a<b and b>a:
    print("true")
else:
    print("false")'''

    
        

    
    
