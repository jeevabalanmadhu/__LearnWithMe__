#Oops - object oriented programming
'''
without oops - procedure calling
with oops - object calling

class - Template or blueprint or outline

class -  collection of methods, variables(local variable, global variable, object)
         formaluas, behaviour and state

class name should be identifier

Method - collection of variables(local)
         formaluas, behaviour and state

method should have a argument(self) which no need to pass

Object is nothing but a address in class

------------------------------
class MyClass:

      def MyMethod(self): #self is a argument which can be anything but no need to be passed while calling
            print("Hi!! I am user defined method")

object_variable=MyClass()
print(object_variable)
object_variable.MyMethod()

output:
<__main__.MyClass object at 0x00000006F7501710>
Hi!! I am user defined method
-------------------------------


class MyClass:

      def MyMethod(self): #self is a argument which can be anything but no need to be passed while calling
            print("Hi!! I am user defined method")

def main(): #function name should be identifier
      object_variable=MyClass()
      print(object_variable)
      object_variable.MyMethod()

if __name__=="__main__":#this is default to call class
      main()

output:
<__main__.MyClass object at 0x000000D3CE4A1710>
Hi!! I am user defined method

-------------------------------

class MyClass:
      name="Rose"
      def MyMethod(self):
            print("Hi!! I am user defined method")
      def Square(self,x):
            print(x**2)
      def SQRT(self,x):
            return x**0.5
      def isOdd(self,x):
            if x%2==1:
                  print("True")
            else:
                  print("False")
def main():
      object_variable=MyClass()
      print(object_variable)
      object_variable.MyMethod()
      object_variable.Square(3)
      print(object_variable.SQRT(9))
      object_variable.isOdd(5)
      print(object_variable.name)

if __name__=="__main__":
      main()

----------------------------------






