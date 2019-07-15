#Conditional statements or Decision making

#colon(:) is for block indentation.
"""
number=int(input("Enter a number:"))

if number==0:
      print("entered number is zero".format(number))

elif number>0:
      print("{} is positive number".format(number))

elif number<0:
      print("{} is negative number".format(number))


if number==0:
      print("entered number is zero".format(number))

elif number%2==0:
      print("{} is even number".format(number))

elif number%2==1:
      print("{} is odd number".format(number))


username=input("Enter your username: ")
password=input("Enter your password: ")

if username == "admin" and password=="admin@123":
      print("Login success")

elif username=="" and password=="":
      print("Input empty, please enter username, password and submit")

elif username!="admin" or password!="admin@123":
      print("invalid credentials entered, please enter valid credentials")


number=int(input("Enter a number:"))

myList=[1,2,3,4,5]
if number in myList:
      print("entered number is in list")

else:
      print("entered number is not in list")

"""
myString="Jeeva"
for item in myString:
      print(item)
