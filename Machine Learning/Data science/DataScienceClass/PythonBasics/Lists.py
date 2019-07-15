#Lists
'''
1. Stored collection of different data types
2. We can modify
3. Mutable
4. Addressing(Indexing) in order manner
5. Random access possible
6. Duplicate possible


---------------------

MyList=[45,67.89, 4+9j,"Data",True,None]

print(MyList)
print("\nList access using possitive index")
print(MyList[0])
print(MyList[1])
print(MyList[2])
print(MyList[3])
print(MyList[4])
print(MyList[5])

output:
[45, 67.89, (4+9j), 'Data', True, None]

List access using possitive index
45
67.89
(4+9j)
Data
True
None

----------------------

MyList=[45,67.89, 4+9j,"Data",True,None]

print(MyList)
print("\nList access using possitive index")
print(MyList[0])
print(MyList[1])
print(MyList[2])
print(MyList[3])
print(MyList[4])
print(MyList[5])
print(MyList[7])

output:
[45, 67.89, (4+9j), 'Data', True, None]

List access using possitive index
45
67.89
(4+9j)
Data
True
None
Traceback (most recent call last):
  File "C:/Users/HP1/AppData/Local/Programs/Python/Python37/Lists.py", line 45, in <module>
    print(MyList[7])
IndexError: list index out of range
------------------


#negative indexing

MyList=[45,67.89, 4+9j,"Data",True,None]

print(MyList)
print("\nList access using possitive index")
print(MyList[-6])
print(MyList[-5])
print(MyList[-4])
print(MyList[-3])
print(MyList[-2])
print(MyList[-1])
print(MyList[-7])

output:
List access using possitive index
45
67.89
(4+9j)
Data
True
None
Traceback (most recent call last):
  File "C:/Users/HP1/AppData/Local/Programs/Python/Python37/Lists.py", line 76, in <module>
    print(MyList[-7])
IndexError: list index out of range
-----------------

#MyList Slicing
MyList=[45,67.89, 4+9j,"Data",True,None]

print(MyList[0:6])
print(MyList[0:6:1])
print(MyList[:6:1])
print(MyList[0::1])
print(MyList[0::])

output:
[45, 67.89, (4+9j), 'Data', True, None]
[45, 67.89, (4+9j), 'Data', True, None]
[45, 67.89, (4+9j), 'Data', True, None]
[45, 67.89, (4+9j), 'Data', True, None]
[45, 67.89, (4+9j), 'Data', True, None]
--------------
MyList=[45,67.89, 4+9j,"Data",True,None]

print(MyList[0:6:1])
print(MyList[0:6:2])
print(MyList[0:6:3])
print(MyList[0:6:4])
print(MyList[0:6:5])
print(MyList[0:6:6])

output:
[45, 67.89, (4+9j), 'Data', True, None]
[45, (4+9j), True]
[45, 'Data']
[45, True]
[45, None]
[45]

----------------------

#List reverse printing

MyList=[45,67.89, 4+9j,"Data",True,None]

print(MyList[5::-1])
print(MyList[-6::1])
print(MyList[-1:-7:-1])

output:
[None, True, 'Data', (4+9j), 67.89, 45]
[45, 67.89, (4+9j), 'Data', True, None]
[None, True, 'Data', (4+9j), 67.89, 45]
--------------------


#List Length

MyList=[45,67.89, 4+9j,"Data",True,None]

print(len(MyList))

output:
6
------------------------



#Delete List
#List Length

MyList=[45,67.89, 4+9j,"Data",True,None]

del(MyList)
print(MyList)

output:
Traceback (most recent call last):
  File "C:/Users/HP1/AppData/Local/Programs/Python/Python37/Lists.py", line 160, in <module>
    print(MyList)
NameError: name 'MyList' is not defined

-------------------


#List Modification

MyList=[45,67.89, 4+9j,"Data",True,None]

MyList=MyList*2

print(MyList)

output:
[45, 67.89, (4+9j), 'Data', True, None, 45, 67.89, (4+9j), 'Data', True, None]

-------------------


#Using built-in functions
#list clear

MyList=[45,67.89, 4+9j,"Data",True,None]

print(MyList)

MyList.clear()

print(MyList)

output
[45, 67.89, (4+9j), 'Data', True, None]
[]

-------------------


#Append

MyList=[45,67.89, 4+9j,"Data",True,None]

print(MyList)

MyList.append("orange")

print(MyList)

output:
[45, 67.89, (4+9j), 'Data', True, None]
[45, 67.89, (4+9j), 'Data', True, None, 'orange']

-------------------

#Pop

MyList=[45,67.89, 4+9j,"Data",True,None]

print(MyList)

MyList.pop()

print(MyList)

MyList.pop(2)

print(MyList)

output:
[45, 67.89, (4+9j), 'Data', True, None]
[45, 67.89, (4+9j), 'Data', True]
[45, 67.89, 'Data', True]

-------------------

#Count

MyList=[45,67.89, 4+9j,"Data",True,None,"Data"]

print(MyList.count("Data"))

output:
2

-------------------

#Index

MyList=[45,67.89, 4+9j,"Data",True,None,"Data"]

print(MyList.index("Data"))

output:
3

#show only the first occurance
-------------------


#Insert

MyList=[45,67.89, 4+9j,"Data",True,None,"Data"]

print(MyList)

MyList.insert(1,"jeeva")

print(MyList)

output:
[45, 67.89, (4+9j), 'Data', True, None, 'Data']
[45, 'jeeva', 67.89, (4+9j), 'Data', True, None, 'Data']

-------------------


#Remove

MyList=[45,67.89, 4+9j,"Data",True,None,"Data"]

MyList.remove("Data")

print(MyList)

output:
[45, 67.89, (4+9j), True, None, 'Data']

#show only the first occurance

-------------------


#reverse

MyList=[45,67.89, 4+9j,"Data",True,None,"Data"]

MyList.reverse()

print(MyList)

output:
['Data', None, True, 'Data', (4+9j), 67.89, 45]

-------------------

#Copy

MyList=[45,67.89, 4+9j,"Data",True,None,"Data"]

print(MyList)
print(id(MyList))

y=MyList
x=MyList.copy()

print(x)
print(id(x))

print(y)
print(id(y))

output:
[45, 67.89, (4+9j), 'Data', True, None, 'Data']
68258333384
[45, 67.89, (4+9j), 'Data', True, None, 'Data']
68258333256
[45, 67.89, (4+9j), 'Data', True, None, 'Data']
68258333384

-------------------


#Sort
#data type should be same in the list

MyList=[45,67.89, 4, 788]

MyList.sort()

print(MyList)

MyList.sort(reverse=True)

print(MyList)

output:
[4, 45, 67.89, 788]
[788, 67.89, 45, 4]

-------------------
'''
