#OOP Encapsulation

'''
1. public - variable or method can be identifier and called from inside or outside class
2. private - variable or method should start with double underscore(ex: __name),
            this can be called only from inside class and must use self with dot operator
            (ex: self.__name or self.__myMethod)

class MyClass:
      def __init__(self):
            print("Hi!! I am constructor")

      def publicMethod(self):
            print("\n  I am a public method")

      def __privateMethod(self):
            print("\n I am a private method")
      
      def __del__(self):
            print("Hi!! I am distructor")

def Main():
      ob=MyClass()
      ob.publicMethod()
      ob.__privateMethod()
      print("GoodBye")
      

if __name__=="__main__":
      Main()

output:
Hi!! I am constructor

  I am a public method
Traceback (most recent call last):
  File "C:/Users/HP1/AppData/Local/Programs/Python/Python37/Encapsulation.py", line 32, in <module>
    Main()
  File "C:/Users/HP1/AppData/Local/Programs/Python/Python37/Encapsulation.py", line 27, in Main
    ob.__privateMethod()
AttributeError: 'MyClass' object has no attribute '__privateMethod'

---------------------------

class MyClass:
      
      def __init__(self):
            print("Hi!! I am constructor")
            self.publicMethod()
            self.__privateMethod()

      def publicMethod(self):
            print("\n  I am a public method")

      def __privateMethod(self):
            print("\n I am a private method")
      
      def __del__(self):
            print("Hi!! I am distructor")

def Main():
      ob=MyClass()
      ob.publicMethod()
      print("GoodBye")
      

if __name__=="__main__":
      Main()

output:
Hi!! I am constructor

  I am a public method

 I am a private method

  I am a public method
GoodBye
Hi!! I am distructor

------------------------------
'''
class MyClass:

      name1="Jeeva" #public variable
      __name2="balan" #private variabe
      
      def __init__(self):
            print("Hi!! I am constructor")
            self.publicMethod()
            self.__privateMethod()

      def publicMethod(self):
            print("\n  I am a public method")

      def __privateMethod(self):
            print("\n I am a private method")
      
      def __del__(self):
            print("Hi!! I am distructor")

def Main():
      ob=MyClass()
      ob.publicMethod()
      print("GoodBye")
      print(ob.name1)
      print(ob.__name2)
      

if __name__=="__main__":
      Main()

'''

output:
Hi!! I am constructor

  I am a public method

 I am a private method

  I am a public method
GoodBye
Jeeva
Traceback (most recent call last):
  File "C:/Users/HP1/AppData/Local/Programs/Python/Python37/Encapsulation.py", line 113, in <module>
    Main()
  File "C:/Users/HP1/AppData/Local/Programs/Python/Python37/Encapsulation.py", line 109, in Main
    ob.__name2
AttributeError: 'MyClass' object has no attribute '__name2'

-------------------------------


class MyClass:

      name1="Jeeva" #public variable
      __name2="balan" #private variabe
      
      def __init__(self):
            print("Hi!! I am constructor")
            self.publicMethod()
            self.__privateMethod()

      def publicMethod(self):
            print("\n  I am a public method")

      def __privateMethod(self):
            print("\n I am a private method")
      
      def __del__(self):
            print("Hi!! I am distructor")
            print(self.name1)
            print(self.__name2)

def Main():
      ob=MyClass()
      ob.publicMethod()
      print("GoodBye")

      

if __name__=="__main__":
      Main()


output:
Hi!! I am constructor

  I am a public method

 I am a private method

  I am a public method
GoodBye
Hi!! I am distructor
Jeeva
balan

----------------------------------------------

'''





