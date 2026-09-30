Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#dictionary{},the data is given in pair format
a={"name":"tanuja","month":9}
a
{'name': 'tanuja', 'month': 9}
type(a)
<class 'dict'>
#keys
a.keys()
dict_keys(['name', 'month'])
#values
a.values()
dict_values(['tanuja', 9])
#items
a.items()
dict_items([('name', 'tanuja'), ('month', 9)])
#accessing--[] is used and we can use a.get method only keys need to be kept
a={"city":"vjw","area":"mgl"}
a["city"]
'vjw'
a.get("area")
'mgl'
a["vjw"]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a["vjw"]
KeyError: 'vjw'
#pop--need to give key value in ()
a={"city":"vjw","area":"mgl","state":"ap","country":"india"}
a.pop("area")
'mgl'
a
{'city': 'vjw', 'state': 'ap', 'country': 'india'}
#popitem - to remove last element
a.popitem()
('country', 'india')
a
{'city': 'vjw', 'state': 'ap'}
#update-to add data,for more data we need keep in single {}
a={"city":"vjw","area":"mgl","state":"ap","country":"india"}
a.update({"year":2026})
a
{'city': 'vjw', 'area': 'mgl', 'state': 'ap', 'country': 'india', 'year': 2026}
a.update({"month":"sep","date":30})
a
{'city': 'vjw', 'area': 'mgl', 'state': 'ap', 'country': 'india', 'year': 2026, 'month': 'sep', 'date': 30}
#setdefault- only one data,eveb if we give without: it aranges ny default
a={"date":30,"time":12}
a.setdefault("month":"sep")
SyntaxError: invalid syntax
a.setdefault("month","sep")
'sep'
a
{'date': 30, 'time': 12, 'month': 'sep'}
#copy,len,clear no count and index
a={"city":"vjw","area":"mgl"}
>>> a.copy()
{'city': 'vjw', 'area': 'mgl'}
>>> len(a)
2
>>> a.count("area")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.count("area")
AttributeError: 'dict' object has no attribute 'count'
>>> a.index("city")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.index("city")
AttributeError: 'dict' object has no attribute 'index'
>>> a.clear()
>>> a
{}
>>> #duplicates--no dup are allowed
>>> a={"city":"vjw","area":"mgl","city":"gtr"}
>>> a
{'city': 'gtr', 'area': 'mgl'}
>>> a={"city1":"vjw","area":"mgl","city2":"gtr"}
>>> a
{'city1': 'vjw', 'area': 'mgl', 'city2': 'gtr'}
>>> #if we want duplicates we need to give diff key name
>>> #single key multiple values we need give values in list[]
>>> a={"idnos":[1,2,3,4},"names":["hi","bell","caira"]}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a={"idnos":[1,2,3,4],"names":["hi","bell","caira"]}
>>> a
{'idnos': [1, 2, 3, 4], 'names': ['hi', 'bell', 'caira']}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names'])
>>> a.values()
dict_values([[1, 2, 3, 4], ['hi', 'bell', 'caira']])
>>> a.items()
dict_items([('idnos', [1, 2, 3, 4]), ('names', ['hi', 'bell', 'caira'])])
