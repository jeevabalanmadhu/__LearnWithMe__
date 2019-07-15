#String handling

#isupper

'''
MyString="HELLO"
MyString1="HELLO%&^%&"
MyString2="HELLO%e"

result=MyString.isupper()
result1=MyString1.isupper()
result2=MyString2.isupper()

print(result)
print(result1)
print(result2)


output:
True
True
False

---------------------

#islower

MyString="hello"
MyString1="hello%&^%&"
MyString2="hello%E"

result=MyString.islower()
result1=MyString1.islower()
result2=MyString2.islower()

print(result)
print(result1)
print(result2)

output:
True
True
False

---------------------


#isspace

MyString=""
MyString1="       "
MyString2="       e"


result=MyString.isspace()
result1=MyString1.isspace()
result2=MyString2.isspace()

print(result)
print(result1)
print(result2)


MyString3=None
result3=MyString3.isspace()
print(result3)


output:
False
True
False
Traceback (most recent call last):
  File "C:/Users/HP1/AppData/Local/Programs/Python/Python37/StringHandling.py", line 65, in <module>
    result3=MyString3.isspace()
AttributeError: 'NoneType' object has no attribute 'isspace'

---------------------

#isdigit

MyString="52342423"
MyString1="2343242 "
MyString2="233423468e3222"


result=MyString.isdigit()
result1=MyString1.isdigit()
result2=MyString2.isdigit()

print(result)
print(result1)
print(result2)

MyString3=""
result3=MyString3.isdigit()
print(result3)

output:
True
False
False
False

---------------------

#istitle

MyString="Hello Python Class"
MyString1="hello Python Class"
MyString2="Hello python Class"


result=MyString.istitle()
result1=MyString1.istitle()
result2=MyString2.istitle()

print(result)
print(result1)
print(result2)


output:
True
False
False

---------------------

#isidentifier


MyString="Hello"
MyString1="hello8"
MyString2="_hello"
MyString3=" hello"
MyString4="^hello"

result=MyString.isidentifier()
result1=MyString1.isidentifier()
result2=MyString2.isidentifier()
result3=MyString3.isidentifier()
result4=MyString4.isidentifier()

print(result)
print(result1)
print(result2)
print(result3)
print(result4)


output:
True
True
True
False
False

---------------------

#isalpha


MyString="Hello"
MyString1="hello8"
MyString2="_hello"
MyString3=" hello"
MyString4="^hello"

result=MyString.isalpha()
result1=MyString1.isalpha()
result2=MyString2.isalpha()
result3=MyString3.isalpha()
result4=MyString4.isalpha()

print(result)
print(result1)
print(result2)
print(result3)
print(result4)

output:
True
False
False
False
False

---------------------

#isalnum


MyString="Hello"
MyString1="hello8"
MyString2="_hello"
MyString3=" hello"
MyString4="^hello"

result=MyString.isalnum()
result1=MyString1.isalnum()
result2=MyString2.isalnum()
result3=MyString3.isalnum()
result4=MyString4.isalnum()

print(result)
print(result1)
print(result2)
print(result3)
print(result4)

output:
True
True
False
False
False

---------------------
#upper

MyString="Hello python"
MyString1="hello8 Py"
MyString2="_hello"
MyString3=" hello"
MyString4="^hello"

result=MyString.upper()
result1=MyString1.upper()
result2=MyString2.upper()
result3=MyString3.upper()
result4=MyString4.upper()

print(result)
print(result1)
print(result2)
print(result3)
print(result4)

output:
HELLO PYTHON
HELLO8 PY
_HELLO
 HELLO
^HELLO

---------------------

#swapcase

MyString="Hello pYthon"
MyString1="hello8 Py"
MyString2="_hELlo"
MyString3=" hello"
MyString4="^hellO"

result=MyString.swapcase()
result1=MyString1.swapcase()
result2=MyString2.swapcase()
result3=MyString3.swapcase()
result4=MyString4.swapcase()

print(result)
print(result1)
print(result2)
print(result3)
print(result4)

output:
hELLO PyTHON
HELLO8 pY
_HelLO
 HELLO
^HELLo

---------------------

#capitalize

MyString="python Class"
MyString1="hello Python Class"
MyString2="Hello python Class"
MyString3="_hello"
MyString4=" hello"


result=MyString.capitalize()
result1=MyString1.capitalize()
result2=MyString2.capitalize()
result3=MyString3.capitalize()
result4=MyString4.capitalize()

print(result)
print(result1)
print(result2)
print(result3)
print(result4)

output:
Python class
Hello python class
Hello python class
_hello
 hello

---------------------
#startswith
 
MyString="python Class"
MyString1="hello Python Class"
MyString2="Hello python Class"
MyString3="_hello"
MyString4=" hello"


result=MyString.startswith("he")
result1=MyString1.startswith("he")
result2=MyString2.startswith("he")
result3=MyString3.startswith("he")
result4=MyString4.startswith("he")

print(result)
print(result1)
print(result2)
print(result3)
print(result4)

output:
False
True
False
False
False

---------------------

#endswith

MyString="python CLASS"
MyString1="hello Python Class"
MyString2="Hello python"
MyString3="_hello class "
MyString4=" hello"


result=MyString.endswith("ss")
result1=MyString1.endswith("ss")
result2=MyString2.endswith("ss")
result3=MyString3.endswith("ss")
result4=MyString4.endswith("ss")

print(result)
print(result1)
print(result2)
print(result3)
print(result4)


output:
False
True
False
False
False

---------------------
#split


MyString="python CLASS"
MyString1="hello Python Class"
MyString2="HeLlo python"
MyString3="_hello class "
MyString4=" heLLo"


result=MyString.split("SS")
result1=MyString1.split("o")
result2=MyString2.split("s")
result3=MyString3.split("l")
result4=MyString4.split("L")

print(result)
print(result1)
print(result2)
print(result3)
print(result4)

output:
1
2
0
3
2

---------------------

#split

MyString="python CLASS"
MyString1="hello Python Class"
MyString2="HeLlo python"
MyString3="_hello class "
MyString4=" heLLo"


result=MyString.split("CL")
result1=MyString1.split(" ")
result2=MyString2.split("on")
result3=MyString3.split("L")
result4=MyString4.split("L")

print(result)
print(result1)
print(result2)
print(result3)
print(result4)


output:

['python ', 'ASS']
['hello', 'Python', 'Class']
['HeLlo pyth', '']
['_hello class ']
[' he', '', 'o']

---------------------

#rstrip

MyString="Hello pYthon   "
MyString1="hello8 Py "
MyString2="_hELlo"
MyString3=" hello"
MyString4=" ^hellO"


result=MyString.rstrip()
result1=MyString1.rstrip()
result2=MyString2.rstrip()
result3=MyString3.rstrip()
result4=MyString4.rstrip()

print(result)
print(len(MyString))
print(len(result))
print(result1)
print(len(MyString1))
print(len(result1))
print(result2)
print(len(MyString2))
print(len(result2))
print(result3)
print(len(MyString3))
print(len(result3))
print(result4)
print(len(MyString4))
print(len(result4))

output:
15
Hello pYthon
15
12
hello8 Py
10
9
_hELlo
6
6
hello
6
5
^hellO
7
6

---------------------


#lrstrip

MyString="Hello pYthon   "
MyString1="hello8 Py "
MyString2="_hELlo"
MyString3=" hello"
MyString4=" ^hellO"


result=MyString.rstrip()
result1=MyString1.rstrip()
result2=MyString2.rstrip()
result3=MyString3.rstrip()
result4=MyString4.rstrip()

print(result)
print(len(MyString))
print(len(result))
print(result1)
print(len(MyString1))
print(len(result1))
print(result2)
print(len(MyString2))
print(len(result2))
print(result3)
print(len(MyString3))
print(len(result3))
print(result4)
print(len(MyString4))
print(len(result4))


output:
Hello pYthon   
15
15
hello8 Py 
10
10
_hELlo
6
6
hello
6
5
^hellO
7
6

---------------------

#rstrip


MyString="Hello pYthon   "
MyString1="hello8 Py "
MyString2="_hELlo"
MyString3=" hello"
MyString4=" ^hellO"


result=MyString.rstrip()
result1=MyString1.rstrip()
result2=MyString2.rstrip()
result3=MyString3.rstrip()
result4=MyString4.rstrip()

print(result)
print(len(MyString))
print(len(result))
print(result1)
print(len(MyString1))
print(len(result1))
print(result2)
print(len(MyString2))
print(len(result2))
print(result3)
print(len(MyString3))
print(len(result3))
print(result4)
print(len(MyString4))
print(len(result4))


output:
Hello pYthon
15
12
hello8 Py
10
9
_hELlo
6
6
 hello
6
6
 ^hellO
7
7


























