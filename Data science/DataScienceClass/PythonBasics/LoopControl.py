#Loop control
'''
#'break' will exit the loop and stop loop iteration

for i in range(1,10):
      if (i==5):
            break
      print(i)

output:
1
2
3
4


#'continue' will exit the iteration and go to next iteration

for i in range(1,10):
      if (i==5):
            continue
      print(i)

output:
1
2
3
4
6
7
8
9



#'pass' will not affect the loop and bypass the loop

for i in range(1,10):
      if (i==5):
            pass
      print(i)

output:
1
2
3
4
5
6
7
8
9


#'break' in while loop

i=2
while i<=10:
      if(i==5):
            break
      print(i)
      i+=1

output:
2
3
4


#'continue' in while loop

i=2
while i<=10:
      if(i==5):
            continue
      print(i)
      i+=1

output:
2
3
4
Traceback (most recent call last):
  File "C:/Users/HP1/AppData/Local/Programs/Python/Python37/LoopControl.py", line 73, in <module>
    while i<=10:
KeyboardInterrupt

#the loop continously executing the same. so the loop will run do not stop. control+c will stop.


#'continue' in while loop

i=2
while i<=10:
      if(i==5):
            pass
      print(i)
      i+=1

Ex:1
name = "Jeevabalan"
for c in name:
      if(c=='b'):
            pass
      print(c)

'''


