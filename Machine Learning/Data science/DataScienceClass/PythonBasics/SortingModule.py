#Sorting Module

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
