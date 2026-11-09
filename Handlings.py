####____Handlings______

####_____Error Handling--3
#1.syntax error--compile error
'''for i in range(10)
print(i)'''

#2.run_time error--during execution
'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)
print(a//b)'''#10//0 zero division error
#3.logical Error--error in logic (can't visible)
'''a=10
b=20
print(a-b)

if a>10:
    print("True")''' #not visible

#####____Exception Handling_____
#try----instructions from which are expecting the exceptions
#except---- exceptions are raised in a try block it will handle by this block
#else---optional no exceptions
#finally---always
while True:
    a=int(input("enter"))
    b=int(input("enter"))
    try:
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("np exceptions")
    finally:
        print("always")

