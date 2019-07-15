#Dictionary
'''
* Key & value pair
* (Key, value) is an item
* Addressing unordered manner
* Random access possible
* Duplicate key cannot be possible
* Mutable, value can be modified, item can be removed

Ex:

MyDict={"fname":"jeeva", 'lname':'madhu',1:"rank"}
print(MyDict)

output:
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank'}

---------------


#Dictionary access using indexing

MyDict={"fname":"jeeva", 'lname':'madhu',1:"rank", "age":29}
print(MyDict)

print(MyDict["fname"])
print(MyDict["lname"])
print(MyDict[1])
print(MyDict["age"])

output:
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}
jeeva
madhu
rank
29
---------------------------


#Delete Dictionary variable

MyDict={"fname":"jeeva", 'lname':'madhu',1:"rank", "age":29}

print(MyDict)

del MyDict

print(MyDict)

output:
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}
Traceback (most recent call last):
  File "C:/Users/HP1/AppData/Local/Programs/Python/Python37/Dictionary.py", line 48, in <module>
    print(MyDict)
NameError: name 'MyDict' is not defined

---------------------------

#length of Dictionary variable

MyDict={"fname":"jeeva", 'lname':'madhu',1:"rank", "age":29}

print(MyDict)

print(len(MyDict))

output:
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}
4


-------------------------

#Append

MyDict={"fname":"jeeva", 'lname':'madhu',1:"rank", "age":29}

print(MyDict)

MyDict["Gendre"]="Male"

print(MyDict)

MyDict["fname"]="Balan" #  duplicate key append will override the value, duplicate key will not work

print(MyDict)


output:
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29, 'Gendre': 'Male'}
{'fname': 'Balan', 'lname': 'madhu', 1: 'rank', 'age': 29, 'Gendre': 'Male'}

--------------------


#Built-in functions

print(dir(dict))

['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear',
'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
'setdefault', 'update', 'values']
----------------------------------

#Clear
MyDict={"fname":"jeeva", 'lname':'madhu',1:"rank", "age":29}

print(MyDict)
MyDict.clear()
print(MyDict)

output:
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}
{}
-----------------------------------



#Copy

MyDict={"fname":"jeeva", 'lname':'madhu',1:"rank", "age":29}

print(MyDict)
X=MyDict.copy()
print(X)

output:
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}
-----------------------------------

#get

MyDict={"fname":"jeeva", 'lname':'madhu',1:"rank", "age":29}

print(MyDict)
X=MyDict.get("lname")
print(X)

output:
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}
madhu
-----------------------------------

#Items

MyDict={"fname":"jeeva", 'lname':'madhu',1:"rank", "age":29}

print(MyDict)
X=MyDict.items()
print(X)

output:

{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}
dict_items([('fname', 'jeeva'), ('lname', 'madhu'), (1, 'rank'), ('age', 29)])
-----------------------------------


#keys

MyDict={"fname":"jeeva", 'lname':'madhu',1:"rank", "age":29}

print(MyDict)
X=MyDict.keys()
print(X)

output:
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}
dict_keys(['fname', 'lname', 1, 'age'])

-----------------------------------

#values

MyDict={"fname":"jeeva", 'lname':'madhu',1:"rank", "age":29}

print(MyDict)
X=MyDict.values()
print(X)

output:
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}
dict_values(['jeeva', 'madhu', 'rank', 29])

-----------------------------------
#pop

MyDict={"fname":"jeeva", 'lname':'madhu',1:"rank", "age":29}

print(MyDict)
MyDict.pop("lname") #must give key values since the index is unorder
print(MyDict)

output:
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}
{'fname': 'jeeva', 1: 'rank', 'age': 29}

-----------------------------------


#popitem

MyDict={"fname":"jeeva", 'lname':'madhu',1:"rank", "age":29}

print(MyDict)
MyDict.popitem() #remove random item
print(MyDict)

output:
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank'}
-----------------------------------


#SetDefault

MyDict={"fname":"jeeva", 'lname':'madhu',1:"rank", "age":29}

print(MyDict)
MyDict.setdefault("fname","Balan") 
print(MyDict)

output:
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}
{'fname': 'jeeva', 'lname': 'madhu', 1: 'rank', 'age': 29}

--------------------------------

'''

#Homework
#Fromkey



keys=['fname','lname', "age", "rank", "age"]

MyDict={}

MyDict=MyDict.fromkeys(keys)

print(MyDict)

values= ['jeeva', 'madhu', 29, 3]

i=0

for key in MyDict:
      MyDict[key]=values[i]
      i+=1

print(MyDict)





























