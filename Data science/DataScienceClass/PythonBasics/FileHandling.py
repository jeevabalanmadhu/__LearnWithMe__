#File Handling:

'''
open is an in built function for file create,
open or override existing file

-----------------------------

open("C:/Users/HP1/Desktop/data.txt","w")

-----------------------------
#Functions
#write

F=open("C:/Users/HP1/Desktop/data.txt","w")
F.write("Writing some text")
F.close() #Without closing the save will not work

------------------------

#Append

F=open("C:/Users/HP1/Desktop/data.txt","a")
F.write(" check")
F.close()

-------------------------

#Read

F=open("C:/Users/HP1/Desktop/data.txt","r")
data=F.read()
print(data)
F.close()

-------------------------

'''

