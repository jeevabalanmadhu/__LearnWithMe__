#OOPS - Constructors

'''
Constructor does not require object(inbuilt key function= __init__)
Distructor also does not require object but it will clear existing objects(inbuilt key function= __del__)
constructors is the first importent in class
distructors is the last importent in class


------------------------------
#Calling class as an object=distructor will run last

class MyClass:
      def __init__(self):
            print("Hi!! I am constructor")
      def __del__(self):
            print("Hi!! I am distructor")

def Main():
      ob=MyClass()
      print("GoodBye")

if __name__=="__main__":
      Main()

output:
Hi!! I am constructor
GoodBye
Hi!! I am distructor

------------------------------

#Calling class without object

class MyClass:
      def __init__(self):
            print("Hi!! I am constructor")
      def __del__(self):
            print("Hi!! I am distructor")

def Main():
      MyClass() #Calling class without object
      print("GoodBye")

if __name__=="__main__":
      Main()

output:
Hi!! I am constructor
Hi!! I am distructor
GoodBye


------------------------------
'''


























      
