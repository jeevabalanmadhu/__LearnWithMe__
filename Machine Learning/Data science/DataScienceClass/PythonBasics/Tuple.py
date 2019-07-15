#Tuple
'''
* Collection of different datatypes
* It cannot modify
* Immutable
* Addressing in order manner(Indexing)
* Random access possible
* Duplicate is possible
----------------------------------
Example :1

MyTuple=(12, "data", 6+2j, None, True)
print(MyTuple)

print("\nTuple access using positive index")

print(MyTuple[0])
print(MyTuple[1])
print(MyTuple[2])
print(MyTuple[3])
print(MyTuple[4])

print("\nTuple access using Negative index")

print(MyTuple[-5])
print(MyTuple[-4])
print(MyTuple[-3])
print(MyTuple[-2])
print(MyTuple[-1])

print("\ntuple index out of range")
      
print(MyTuple[5])

output:
(12, 'data', (6+2j), None, True)

Tuple access using positive index
12
data
(6+2j)
None
True

Tuple access using Negative index
12
data
(6+2j)
None
True

tuple index out of range
Traceback (most recent call last):
  File "C:/Users/HP1/AppData/Local/Programs/Python/Python37/Tuple.py", line 33, in <module>
    print(MyTuple[5])
IndexError: tuple index out of range


---------------------------
#Slicing:

Ex:1

#MyTuple Slicing
MyTuple=(45,67.89, 4+9j,"Data",True,None)

print(MyTuple[0:6])
print(MyTuple[0:6:1])
print(MyTuple[:6:1])
print(MyTuple[0::1])
print(MyTuple[0::])

output:

(45, 67.89, (4+9j), 'Data', True, None)
(45, 67.89, (4+9j), 'Data', True, None)
(45, 67.89, (4+9j), 'Data', True, None)
(45, 67.89, (4+9j), 'Data', True, None)
(45, 67.89, (4+9j), 'Data', True, None)

Ex:2
--------------------------

#MyTuple Slicing
MyTuple=(45,67.89, 4+9j,"Data",True,None)

print(MyTuple[1:6])
print(MyTuple[1:6:2])
print(MyTuple[1:6:3])
print(MyTuple[1:6:4])
print(MyTuple[1:6:5])

output:
(67.89, (4+9j), 'Data', True, None)
(67.89, 'Data', None)
(67.89, True)
(67.89, None)
(67.89,)
--------------------------

#Delete tuple

MyTuple=(45,67.89, 4+9j,"Data",True,None)

print(MyTuple)

del MyTuple

print(MyTuple)

----------------------------

#Length of tuple

MyTuple=(45,67.89, 4+9j,"Data",True,None)

print(MyTuple)

print(len(MyTuple))

output:
(45, 67.89, (4+9j), 'Data', True, None)
6
----------------------------
'''

#Tupe immutable
'''
MyTuple. clear, append, insert, copy will not work and throw error stating that
tuple does have the attribute.

tuple attributes are


print(dir(tuple))

['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
'__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', 'count', 'index']

---------------------------

#Tuple count

MyTuple=(45,67.89, 4+9j,"Data",True,None,"Data")

print(MyTuple.count("Data"))

output:
2
---------------------------


#Tuple Index

MyTuple=(45,67.89, 4+9j,"Data",True,None,"Data")

print(MyTuple.index("Data"))

output:
3
#first element of index will display as output

--------------------------
'''




