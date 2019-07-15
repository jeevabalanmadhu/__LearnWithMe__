#Sorting of ListNumbers

n=int(input("count of ListNumbers: "))
numbers=[]

TypeSorting=input("Accending or Decending: ")

i=0
while(i<n):
      numbers.insert(i,input("Enter numbers of {}:".format(i+1)))
      i+=1
print(numbers)

def accending(ListNumbers):
      n=len(ListNumbers)

      i=0

      while(i<n):
            j=i+1
            while(j<n):
                  if(ListNumbers[i]>ListNumbers[j]):
                        a=ListNumbers[i]
                        ListNumbers[i]=ListNumbers[j]
                        ListNumbers[j]=a
                  
                  j+=1
            i+=1
      return ListNumbers

def decending(ListNumbers):
      n=len(ListNumbers)

      i=0

      while(i<n):
            j=i+1
            while(j<n):
                  if(ListNumbers[i]<ListNumbers[j]):
                        a=ListNumbers[i]
                        ListNumbers[i]=ListNumbers[j]
                        ListNumbers[j]=a
                  
                  j+=1
            i+=1
      return ListNumbers


if(TypeSorting=="Accending"):
      accending(numbers)
      print("Sorting in accending order:",numbers)
elif(TypeSorting=="Decending"):
      decending(numbers)
      print("Sorting in decending order:",numbers)
else:
      print("incorrect input of sorting type, please run again")




