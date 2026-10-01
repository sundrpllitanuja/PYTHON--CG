Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #Indexing--accessing individual items within an ordered sequence by refering a position
>>> #+ve indexing
>>> a="i am in class"
>>> a[8]+a[9]+a[10]+a[11]+a[12]
'class'
>>> a[2]+a[3]
'am'
>>> a[1]
' '
>>> a[0]
'i'
>>> b="vijayawada has various food spots"
>>> b[2]+b[3]
'ja'
>>> b[11]+b[12]+b[13]
'has'
>>> #-ve indexing
>>> a="vijayawada has various food spots"
>>> a[-11]+a[-12]+a[-13]
' su'
>>> a[-10]+a[-9]+a[-8]+a[-7]
'food'
>>> 
>>> #Slicing--allows us to create a subset
>>> #[:4]--start to upto 4 position
>>> #[7:]--7 position to very end
>>> #a[:]-- all prints
>>> #[::2]-- every second digit is soln
>>> #[::-1]--reverse the process and 2nd digit is the soln
>>> #[4:10:2]-- the first digit is the starting point, second digit is the ending point and the third digit is the step.
>>> #the process is called as striding there will step process
>>> a="codegnan"
>>> a[0:4]
'code'
>>> a[5:8]
'nan'
>>> a[:4]
'code'
>>> a[6:]
'an'
>>> #-ve slicing
>>> a="Today is weekend"
>>> a[-16:-11]
'Today'
a=[-7]
a=[-7:]
SyntaxError: invalid syntax
a=[-6:]
SyntaxError: invalid syntax
a[-1]
-7
a[-7]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a[-7]
IndexError: list index out of range
a[-7:]
[-7]
a="Today is weekend"
a[-7:]
'weekend'
#striding--
a="Machine Learning"
a[::4]
'MiLn'
a[::6]
'Men'
b="cloud computing"
b[3:10:4]
'uo'
#-ve striding
a="Python Course"
a[-7:-11:-2]
' o'

a[-1:-11:-2]
'ero o'
