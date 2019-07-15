#Exception handling or Run time error handling

# Try---except:
'''
a=5
b=4
division=a/b
print(division)

print("good bye")

output:
1.25
good bye

-----------


a=5
b=0
division=a/b
print(division)

print("good bye")

output:
Traceback (most recent call last):
  File "C:/Users/HP1/AppData/Local/Programs/Python/Python37/Exception handling.py", line 21, in <module>
    division=a/b
ZeroDivisionError: division by zero
-----------

a=5
b=0

try:
      division=a/b
      print(division)

except:
      print("error occurred")

     
print("good bye")

output:
error occurred
good bye

-----------

a=5

try:
      division=a/b
      print(division)

except Exception as e:
      print("error occurred")
      print(e)


print("good bye")

output:
error occurred
name 'b' is not defined
good bye

-----------

a=[5,3,5]

try:
      print(b)
      print(a[0])
      print(a[1])
      print(a[2])
      print(a[3])
      
except IndexError as i:
      print("Index error")

except Exception as e:
      print("error occurred")
      print(e)


print("good bye")

-----------

a=(5,3,5)

try:
      
      print(a[0])
      print(a[1])
      print(a[2])
      print(a[3])
      
except IndexError as i:
      print("Index error")

except Exception as e:
      print("error occurred")
      print(e)


print("good bye")

-----------

a="joy"

try:
      
      print(a[0])
      print(a[1])
      print(a[2])
      print(a[3])
      
except IndexError as i:
      print(i)

print("good bye")

output:
j
o
y
string index out of range
good bye

--------------------
'''
a={"name":"joy"}

try:
      
      print(a["name"])
      print(a["joy"])
      
except KeyError as i:
      print("key error:",i)

print("good bye")




