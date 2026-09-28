Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#String Methods
#len- no.of characters in a given string
a="python"
len(a)
6
b="pyhton full stack"
len(b)
17
c=""
len(c)
0
d=" "
len(d)
1
#Count- no.of repeated characters in string
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("l")
4
a.count(" ")
3
#Find the string
a="python"
a.find("h")
3
a[3]
'h'
b="hello"
b.find("l")
2
#not possible to get 2-l at a time in this we need to use slicing
b[2:4]
'll'
#Escape sequences-2types
#\n->new line
#
#\t->tab space
a="name\nphn num\tcollege\nmailid\tbranch"
print(a)
name
phn num	college
mailid	branch
b="name:Tanuja\nphn num:1234567890\tcollege:PBSCAS\nmailid:tanu@gmail.com\tbranch:VJW"
print(b)
name:Tanuja
phn num:1234567890	college:PBSCAS
mailid:tanu@gmail.com	branch:VJW
#Replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="python fullstack"
a.replace("fullstack","course")
'wait until you succeed'
b.replace("fullstack","course")
'python course'
a
'wait until you succeed'
c=a.replace("wait","work")
c
'work until you succeed'
#upper()
#lower()
#capitalize-1st letter caps
#title- in a sentence every letter after space is caps
a="code"
a.upper()
'CODE'
b="HELLO"
b.lower()
'hello'
c="assignment"
c.captalize()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    c.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
c.capitalize()
'Assignment'
d="my name is python"
d.title()
'My Name Is Python'
#conditions- using is
a="java"
a.isupper()
False
a.islower()
True
a.startswith("j")
True
a.startswith("s")
False
a.endswith("a")
True
a.isdigit()
False
b="612"
b.isdigit()
True
c="tanu123"
c.isalnum()
True
z="tanu@12"
z.isalnum()
False
type(z)
<class 'str'>
#doesn't allow special characters like @
#strip- used for space in right or left like start or end of the sentence
a="      tanu     "
a.strip()
'tanu'
a.lstrip()
'tanu     '
a.rstrip()
'      tanu'
#concatenation- which adds strings
a="code"
b="gnan"
Print(a+b)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    Print(a+b)
NameError: name 'Print' is not defined. Did you mean: 'print'?
print(a+b)
codegnan

fname="tanu"
lname="s"
print(fname+lname)
tanus
print(fname+" "+lname)
tanu s
print(fname+" "+lname).title()
tanu s
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    print(fname+" "+lname).title()
AttributeError: 'NoneType' object has no attribute 'title'
print((fname+" "+lname).title())
Tanu S
#Split-in a sentence the words are separated by commas
a="c c++ java python"
a.split()
['c', 'c++', 'java', 'python']
b="i am learning java"
b.split()
['i', 'am', 'learning', 'java']
#join()
a='i', 'am', 'learning', 'java'
"".join(a)
'iamlearningjava'
" ".join(a)
'i am learning java'
d="apple"
"l".join(d)
'alplpllle'
#formatting- adding extra data
a=3
b=6
a+b
9
print("the sum is",a+b)
the sum is 9
city="vjw"
print("i live in",city)
i live in vjw
#format method- we can improvise as we like
a="motu"
b="patlu"
print((hello{}{}".format(a,b))
       
SyntaxError: unterminated string literal (detected at line 1)

print("hello {}{}".format(a,b))
       
hello motupatlu
print("hello {} {}".format(a,b))
       
hello motu patlu
print(("hello {} {}".format(a,b)).title())
       
Hello Motu Patlu
print(("hello {} hello{}".format(a,b)).title())
       
Hello Motu Hellopatlu
print(("hello {} hello {}".format(a,b)).title())
       
Hello Motu Hello Patlu
#fstring-
       
a="tanu"
       
b="s"
       
print(f"hello {a} {b}")
       
hello tanu s
print((f"hello {a} {b}").title())
...        
Hello Tanu S
>>> #product of 2 num usibg fstring
...        
>>> a=2
...        
>>> b="2"
...        
>>> c="4"
...        
>>> d=b*c
...        
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    d=b*c
TypeError: can't multiply sequence by non-int of type 'str'
>>> a=2
...        
>>> b=4
...        
>>> c=a*b
...        
>>> print(f"the product is{c}")
...        
the product is8
>>> print(f"the product is {a*b}")
...        
the product is 8
>>> print(f"the product is{}".format(c))
...        
SyntaxError: f-string: valid expression required before '}'
>>> print("the product is{}".format(c))
...        
the product is8
>>> print(f"the product is {}".format(a*b))
...        
SyntaxError: f-string: valid expression required before '}'
>>> print("the product is {}".format(a*b))
...        
the product is 8
