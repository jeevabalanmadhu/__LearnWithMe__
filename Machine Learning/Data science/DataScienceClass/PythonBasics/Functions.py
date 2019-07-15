#Defining a script
'''
Introduction:

1. A function is a self block of code
2. A function can be called as section of a program that is written once and can be executed
   whenever required in the program, thus making code reusability
3. A function is a subprogram that works on data and produce same output.

Types of functions:

There are two type of function.
a) Built-in functions:
      * Functions that are predefined.
      * We have used many predefined functions in python

b) user defined:
      * Functions that are created according to the requirements.



#User defined functions
#procedure call is calling the funtion with this is name

#Funtion declaration

Ex: 1
def myFunction():
      print("Hi.. i am user defined function")

def add():
      a=100 #a, b are local variable in add funciton
      b=200
      print(a+b)

#Function calling
myFunction()
add()
add()

# we can create n number of funtion in package and can call the function n number times based on requirement.

Ex 2:

def add(a=100, b=200): #a, b are arguments and 100, 200 are paraments
      print(a+b)

add()


#Ex 3:

def add(a,b): #a,b - arguments
      print(a+b)

add(100,200) #100, 200 - parameters


#Ex 4:

def add(a,b): #a,b - arguments
      print("a value is:",a)
      print("b value is:",b)
      print(a+b)

add(a=100,b=200) #100, 200 - parameters


#Ex 5:

def add(a,b): #a,b - arguments
      print("a value is:",a)
      print("b value is:",b)
      print(a+b)

add(b=100,a=200) #100, 200 - parameters

output:

a value is: 200
b value is: 100
300


#Ex 6:

def add(a=2,b=3): #a,b - arguments
      print("a value is:",a)
      print("b value is:",b)
      print(a+b)

add(b=100,a=200) #100, 200 - parameters

output:
a value is: 200
b value is: 100
300

# function will take the value from calling function parameters. if parameter is not available, it will take the default value assigned in fucntion


Ex 7:

def add(a=2,b=3): #a,b - arguments
      a=50
      b=60
      print("a value is:",a)
      print("b value is:",b)
      print(a+b)

add(b=100,a=200) #100, 200 - parameters

output:
a value is: 50
b value is: 60
110

#value assigned inside declared funtion will be stored to execute



def add(a=2,b=3): #a,b - arguments
      print("a value is:",a)
      print("b value is:",b)
      print(a+b)

x=10
y=20
add(b=x,a=y) #100, 200 - parameters



####Returing function:

#Function Declaration
def add(a,b): #a,b - arguments
      return a+b

print(add(a=1,b=4))

output:
5



def add(a,b): #a,b - arguments
      return a+b

x=add(a=1,b=4)
print(x-2)

output:
3

'''

