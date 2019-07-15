#odd or even from 1-100
'''

####method: 1

myOddList=[]
myEvenList=[]

for i in range(1,101):
      if(i%2==0):
            print("even = {0}".format(i))
            
      elif(i%2==1):
            print("odd = {0}".format(i))

'''
###Method 2:

myOddList=[]
myEvenList=[]

for i in range(1,101):
      if(i%2==0):
            myEvenList.append(i)
            
      elif(i%2==1):
            myOddList.append(i)

print("Odd number from 1 - 100 are: ",myOddList)
print()
print("Even number from 1 - 100 are: ",myEvenList)



