import SortingModule

n=int(input("count of ListNumbers: "))
numbers=[]

TypeSorting=input("Accending or Decending: ")

i=0
while(i<n):
      numbers.insert(i,input("Enter numbers of {}:".format(i+1)))
      i+=1
print(numbers)


if(TypeSorting=="Accending"):
      SortingModule.accending(numbers)
      print("Sorting in accending order:",numbers)
elif(TypeSorting=="Decending"):
      SortingModule.decending(numbers)
      print("Sorting in decending order:",numbers)
else:
      print("incorrect input of sorting type, please run again")
