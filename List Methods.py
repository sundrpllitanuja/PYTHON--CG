Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#Lists[]
#we can pass any type of data and collection of data
a=[3,4.5,"python",6+9j,True,False]
a
[3, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=1.2
type(b)
<class 'float'>
c=[1.2]
type(c)
<class 'list'>
#append- we cann add one extra data
a=["java","c","c++"]
a.append("ai")
a
['java', 'c', 'c++', 'ai']
a.append("ai","ml")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("ai","ml")
TypeError: list.append() takes exactly one argument (2 given)
#extend- we can add one or more data
a=["java","c","c++"]
a.extend(["ai","ml"])
a
['java', 'c', 'c++', 'ai', 'ml']
#insert- to insert at a particular position
a=["java","c","c++"]
a.insert(2,"ai")
a
['java', 'c', 'ai', 'c++']
#index- tells exact place
a=["hyd","vjw","vizag"]
a.index("vjw")
1
#copy- to copy the data into another variable
c=a.copy()
c
['hyd', 'vjw', 'vizag']
#sort- to arrange in alphabetical order/ either in numbers
a=["mango","apple","kiwi"]
a.sort()
a
['apple', 'kiwi', 'mango']
b=[10,4,8,1,9]
b.sort()
b
[1, 4, 8, 9, 10]
c=["mango","Apple","kiwi","berry","Banana"]
#here in the above we have both upper and lower cases here it takes upper casse as the 1st priority
c.sort()
c
['Apple', 'Banana', 'berry', 'kiwi', 'mango']
#Reverse- prints in reverse
a=["mango","apple","kiwi"]
a.reverse()
a
['kiwi', 'apple', 'mango']
b=[9,2,8,1]
b.reverse()
b
[1, 8, 2, 9]
#pop- deletes the last element or else we can give index number
a=['java', 'c', 'c++', 'ai', 'ml']
a.pop()
'ml'
>>> a
['java', 'c', 'c++', 'ai']
>>> a.pop(1)
'c'
>>> a
['java', 'c++', 'ai']
>>> #remove- we can remove the particular data we want
>>> a=["java","ai","ml","c++"]
>>> a.remove("ai")
>>> a
['java', 'ml', 'c++']
>>> #clear- clears whole data
>>> a=["java","ai","ml","c++"]
>>> a.clear()
>>> a
[]
>>> c=[]
>>> c.append("ds")
>>> c
['ds']
>>> #length- here it takes whole word as 1 but in string it takes each letter
>>> a=["java","c","c++"]
>>> len(a)
3
>>> b="hello"
>>> len(b)
5
>>> c=["hello"]
>>> len(c)
1
>>> #count- it counts words after comma
>>> a=["java","c","c++"]
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> a.count("c++")
1
