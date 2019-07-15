Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #IDLE - Integrated development and learning environment
>>> 
>>> 
>>> #Interactive mode
>>> #Basic Syntax
>>> print("hello world")
hello world
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> print("My name is","Jeeva")
My name is Jeeva
>>> print("my name is","jeeva",sep="")
my name isjeeva
>>> 
>>> myName = "jeeva"
>>> print(myName")
      
SyntaxError: EOL while scanning string literal
>>> print(myName)
jeeva
>>> 
= RESTART: C:\Users\HP1\AppData\Local\Programs\Python\Python37\saveshell.py =
Hi..!
I am 
python programming
>>> 
= RESTART: C:\Users\HP1\AppData\Local\Programs\Python\Python37\saveshell.py =
Hi..!
python programming
>>> 
= RESTART: C:\Users\HP1\AppData\Local\Programs\Python\Python37\saveshell.py =
>>> 
= RESTART: C:\Users\HP1\AppData\Local\Programs\Python\Python37\saveshell.py =
Hi..!
I am 
python programming
>>> 
= RESTART: C:\Users\HP1\AppData\Local\Programs\Python\Python37\saveshell.py =
Hi..!I am 
python programming
>>> 
= RESTART: C:\Users\HP1\AppData\Local\Programs\Python\Python37\saveshell.py =
Hi..! I am 
python programming
>>> 
= RESTART: C:\Users\HP1\AppData\Local\Programs\Python\Python37\saveshell.py =
Hi..! I am 
Traceback (most recent call last):
  File "C:\Users\HP1\AppData\Local\Programs\Python\Python37\saveshell.py", line 4, in <module>
    print(language)
NameError: name 'language' is not defined
>>> 
= RESTART: C:\Users\HP1\AppData\Local\Programs\Python\Python37\saveshell.py =
Hi..! I am 
Python Programming
>>> 
= RESTART: C:\Users\HP1\AppData\Local\Programs\Python\Python37\saveshell.py =
Hi..!
I am 
Python Programming
>>> 
= RESTART: C:\Users\HP1\AppData\Local\Programs\Python\Python37\saveshell.py =
Hi..!
I am 
Python
Programming
>>> 
= RESTART: C:\Users\HP1\AppData\Local\Programs\Python\Python37\saveshell.py =
Hi..!
I am 
Python\nProgramming
>>> 
= RESTART: C:\Users\HP1\AppData\Local\Programs\Python\Python37\saveshell.py =
Hi..!
I am 
Python	Programming
>>> #Data literals
>>> #1. String literals
>>> myString="Jeeva"
>>> type(myString)
<class 'str'>
>>> print(myString)
Jeeva
>>> myString
'Jeeva'
>>> #Multi line string declaration
>>> myString='hello\
Python'
>>> print(myString)
helloPython
>>> myString
'helloPython'
>>> #Multiple line string declaration
>>> myString = """Hello
python
programming"""
>>> myString
'Hello\npython\nprogramming'
>>> print(myString)
Hello
python
programming
>>> #Numeric Declaration
>>> #integer
>>> myInt=100
>>> type(myInt)
<class 'int'>
>>> myInt
100
>>> print(myInt)
100
>>> #Floating
>>> myFloat=3.14
>>> print(myFloat)
3.14
>>> myFloat
3.14
>>> type(myFloat)
<class 'float'>
>>> type(myFloat
     )
<class 'float'>
>>> #Complex
>>> myComplex=4+5j
>>> myComplex
(4+5j)
>>> print(myComplex)
(4+5j)
>>> #Boolean Literals
>>> myBool=True
>>> type(myBool)
<class 'bool'>
>>> print(myBool)
True
>>> myBool
True
>>> #None type literals
>>> myNone=None
>>> type(myNone)
<class 'NoneType'>
>>> print(myNone)
None
>>> myNone
>>> #Tuple-Collection of Data
>>> myTuple=(10, 3.14, "Apple", True, 4+5j, None)
>>> type(myTuple)
<class 'tuple'>
>>> print(myTuple)
(10, 3.14, 'Apple', True, (4+5j), None)
>>> myTuple
(10, 3.14, 'Apple', True, (4+5j), None)
>>> #List-Collection of Different data types
>>> myList=[10,3.14,"my apple", True, 4+3j, None]
>>> type(myList)
<class 'list'>
>>> print(myList)
[10, 3.14, 'my apple', True, (4+3j), None]
>>> myList
[10, 3.14, 'my apple', True, (4+3j), None]
>>> 
= RESTART: C:\Users\HP1\AppData\Local\Programs\Python\Python37\saveshell.py =
Hi..!
I am 
Python	Programming
>>> #Dictionary-Key&Value pair
>>> MyDict={"Name":"Jeeva","Age":29}
>>> MyDict
{'Name': 'Jeeva', 'Age': 29}
>>> type(MyDict)
<class 'dict'>
>>> myDict1={"Name":["Jeeva","Balan"],"Age":[29,30]}
>>> type(myDict1)
<class 'dict'>
>>> myDict1
{'Name': ['Jeeva', 'Balan'], 'Age': [29, 30]}
>>> print(myDict1)
{'Name': ['Jeeva', 'Balan'], 'Age': [29, 30]}
>>> #set
>>> 
mySet={"Apple", 3.14, True, 345}
>>> type(mySet)
<class 'set'>
>>> print(mySet)
{345, True, 3.14, 'Apple'}
>>> mySet
{345, True, 3.14, 'Apple'}
>>> print(mySet)
{345, True, 3.14, 'Apple'}
>>> 
