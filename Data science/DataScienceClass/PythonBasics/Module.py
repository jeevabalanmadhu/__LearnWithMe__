#Python Module:
'''
* Modules are used to categorize python code into smaller parts.
* A module is simply a python file, where classes, functions and variables are defined.
* Grouping similar code into a single file makes it easy to access.

Python module advantage:
1. Reusability: Module can be used in some other python code.
                Hence it provides the facility of reusability.

-----------------------
import MyModule

MyModule.add()
MyModule.square(5)
print(MyModule.sqrt(9))
MyModule.isodd(9)

----------------------

from MyModule import add

add()

output:
300

---------------------

from MyModule import add,square,sqrt,isodd

add()
square(5)
print(sqrt(81))
isodd(9)

output:
300
25
9.0
True

------------------

    
from MyModule import *

add()
square(5)
print(sqrt(81))
isodd(9)

output:
300
25
9.0
True
'''


