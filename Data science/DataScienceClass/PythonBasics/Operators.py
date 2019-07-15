a=12
b=7
"""
print("Arithmetic operators")

print("Addition=", a+b)
print("Seperation=", a-b)
print("Multiplication=", a*b)
print("Division=",a/b)
print("Modulus=",a%b)
print("Floor division=",a//b)
print("Power=",a//b)

print()
print("Assignment operators")
print()
a+=2
b-=1
"""

"""
print("Addition=", a+b)
print("Seperation=", a-b)
print("Multiplication=", a*b)
print("Division=",a/b)
print("Modulus=",a%b)
print("Floor division=",a//b)
print("Power=",a**b)


print()
print("Relative operators")
print()
a=5
b=6

print("Less than=", a<b)
print("Greater than=", a>b)
print("greater than or equal to=", a>=b)
print("less than or equal to=", a<=b)
print("equal to=", a==b)
print("notequal to=", a!=b)


print()
print("logical operators")
print()
a=5
b=6

print("AND=", a>b and b==a)
print("OR=", not a<b)


print("Membership operators")
print()
myList=[2,5,6,7,8]

print (5 in myList)
print ("5" in myList)
print (7 not in myList)


print("Identity operators")
print()

print (5 is 5)
print ("5" is 5)
print (7 is 10)
print (7 is not 10)

print("Bitwise operators")
print()
a=99
b=100

print (a&b)
print (a|b)
print (a^b)
"""

#Getting input form users

a=float(input("enter a number: "))
print(type(a))

b=float(input("enter a number: "))
type(b)
print(type(b))

sum=a+b

print("{0}+{1}={2}".format(a,b,sum))
