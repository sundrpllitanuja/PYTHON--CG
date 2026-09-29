Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#Sets{}
a={3,4.5,"python",6+9j,True,False}
a
{False, True, (6+9j), 3, 4.5, 'python'}
type(a)
<class 'set'>
#sets Methods
a={2,5,7,9,4,8}
a.add(10)
a
{2, 4, 5, 7, 8, 9, 10}
#is subset
b={2,5,7,9,4,8}
c={2,5,7}
c.issubset(b)
True
b.issubset(a)
True
#is superset
a={2,5,7,9,4,8}
b={12,1,13,17}
a.issuperset(b)
False
a={1,2,3,4,5}
b{4,3,5}
SyntaxError: invalid syntax
b={4,3,5}
b.issuperset(a)
False
a.issuperset(a)
True
a={2,8,9,5,1,4,14,19,3}
a
{1, 2, 3, 4, 5, 8, 9, 14, 19}
#union-merging of 2 sets into one
a={1,2,3,4,5}
b={5,6,7,8,9,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#intersection-prints common values in both sets
a={1,2,3,4,5}
b={5,6,7,8,9,10}
a.intersection(b)
{5}
#update-b lo unnavi anni a loki update aitay ippudu manam a type cheste update aina set vachiddi
a={1,2,3,4,5}
b={4,5,6,7,8}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8}
a
{1, 2, 3, 4, 5, 6, 7, 8}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8}
b
{1, 2, 3, 4, 5, 6, 7, 8}
#difference- without merging it take diff values
a={5,6,7,8,9,10,11,12}
b={8,9,10,11,12,13,14}
a.difference(b)
{5, 6, 7}
b.difference(a)
{13, 14}
#symmetric_differnce- same ga unnai del chesi ichiddi
a={5,6,7,8,9,10,11,12}
b={8,9,10,11,12,13,14}
a.symmetric_difference(b)
{5, 6, 7, 13, 14}
#difference_update
a={5,6,7,8,9,10,11,12}
b={8,9,10,11,12,13,14}
a.difference_update(b)
a
{5, 6, 7}
b.difference_update(a)
b
{8, 9, 10, 11, 12, 13, 14}
#intersection_update
a={5,6,7,8,9,10,11,12}
b={8,9,10,11,12,13,14}
a.intersection_update(b)
a
{8, 9, 10, 11, 12}
b.intersection_update(a)
b
{8, 9, 10, 11, 12}
#symmetric_diff_update
a={10,20,30,40,50}
b={30,40,50,60,70}
a.symmetric_difference_update(b)
a
{20, 70, 10, 60}
b.symmetric_difference_update(a)

b
{50, 20, 40, 10, 30}


#pop and remove
a={2,3,4,5,6,7}
a.pop()
2
a
{3, 4, 5, 6, 7}
a.remove(5)
a
{3, 4, 6, 7}
#discard and remove are same
a.discard(4)
a
{3, 6, 7}
#clear
a.clear()
a
set()
#to add data
b.add(60)
b
{50, 20, 40, 10, 60, 30}
a.add(60)
a
{60}
>>> #is disjoint
>>> a={1,2,3,4}
>>> b={5,6,7,8}
>>> a.isdisjoint(b)
True
>>> #length,count-no count(doesn't allow duplicate values,index-no index
>>> a={1,2,3,4}
>>> len(a)
4
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'
>>> a.index()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    a.index()
AttributeError: 'set' object has no attribute 'index'
>>> 
>>> 
>>> #Tuple-it is immutable,(),collection of datatypes
>>> a=(1,2.3,"tanu",1+7j,True,False)
>>> a
(1, 2.3, 'tanu', (1+7j), True, False)
>>> type(a)
<class 'tuple'>
>>> 
>>> #Methods-count and index
>>> a.count(tanu)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a.count(tanu)
NameError: name 'tanu' is not defined
>>> a.count(1+7j)
1
>>> a.index(True)
0
