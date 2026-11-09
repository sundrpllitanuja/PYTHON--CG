Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
print(4+8)
12
a=10
print(a)
10
x=50
print(x)
50
0123456789=100
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a01234567=100
print(a1234567)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(a1234567)
NameError: name 'a1234567' is not defined. Did you mean: 'a01234567'?
name="tanu"
print(name)
tanu
print("name")
name
city=vja
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    city=vja
NameError: name 'vja' is not defined
city="vja"
print(city)
vja
fname=sai
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    fname=sai
NameError: name 'sai' is not defined
fname="sai"
lname="ram"
print(fname+lname)
sairam
print(fname+" "+lname)
sai ram
a=3,b=2
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=3;b=2
print(a+b)
5
a,b=4,5
print(a+b)
9
>>> @=10
SyntaxError: invalid syntax
>>> _=10
>>> print(_)
10
>>> _A=200
>>> print(_A)
200
>>> if=20
SyntaxError: invalid syntax
>>> while=20
SyntaxError: invalid syntax
>>> a=2,3,4,5,6,7,8
>>> print(a)
(2, 3, 4, 5, 6, 7, 8)
>>> a,b,c=1,2,3
>>> print(a,b,c)
1 2 3
>>> a,b,c=1,2,3,4,5
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a,b,c=1,2,3,4,5
ValueError: too many values to unpack (expected 3, got 5)
>>> first name="tanu"
SyntaxError: invalid syntax
>>> first_name="tanu"
>>> print(first_name)
tanu
>>> # Python automatically converts the int to float
>>> num_int = 10num_float = 5.5
SyntaxError: invalid decimal literal
>>> num_int = 10num_float = 5.5
SyntaxError: invalid decimal literal
>>> num_int = 10
>>> num_float = 5.5
>>> result = num_int + num_float
>>> print(result)
15.5
>>> print(type(result))
<class 'float'>
