Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #operators
>>> #assignment
>>> a=5
>>> b=3
>>> a+b
8
>>> a-b
2
>>> a*b
15
>>> a//b
1
>>> a/b
1.6666666666666667
>>> a**b
125
>>> a%b
2
>>> #assignment
>>> a=7
>>> b=4
>>> a+=b
>>> 
>>> a
11
>>> a-=b
>>> a
7
>>> a*=b
>>> a
28
>>> a//=b
>>> a
7
>>> a/=b
>>> a
1.75
>>> a**=b
>>> a
9.37890625
>>> a%=b
>>> a
1.37890625
>>> #comparision
>>> a=2
>>> b=4
>>> a>b
False
>>> a<b
True
>>> a>=b
False
>>> a<=b
True
>>> a!=b
True
>>> a==b
False
>>> #logical
>>> a=10
>>> b=20
>>> a<b and b>a
True
>>> a<=b and b>=a
True
>>> a!=b and a==b
False
>>> a<b or b>a
True
a<=b or b>=a
True
a!=b or a==b
True
#identify
A=10
type (A) is int
True
type (A) is not int
False
type(A)is float
False
B=2.3
type(B) is float
True
c="car"
type(c) is not string
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    type(c) is not string
NameError: name 'string' is not defined. Did you forget to import 'string'?
type(c) is not str
False
type(c) is str
True
m=1j+2
type(m) is complex
True
a=false
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a=false
NameError: name 'false' is not defined. Did you mean: 'False'?
a=False
type (a) is bool
True
#membership
a=2,3,4,5,6
2 in a
True
8 in a
False
8 not in a
True
#bitwise
a=2
b=4
bin(a)
'0b10'
bin(b)
'0b100'
a&b
0
#or
a=2
b=4
a|b
6
a=4
b=8
a|b
12
#neg ~
a=5
-(a+1)
-6
~a
-6
b=-10
~b
9
#x-or 2same=0 2opp=1
a=3
b=5
a^b
6
#<<
a=4
a<<2
16
#>>
a=4
a>>2
1
