   1  a=int(input("enter the terms"))
   2  f=0
   3  s=1
   4  ifa<=0:
   5  print("the requested series is",f)
   6  else:
   7  print(f,s,end="")
   8  for x in range(2,a):
   9  next=f+s
  10  print(next,end="")
  11  f=s
  12  s=next
  13  enter the terms =13
  14. 0,1,1,2,3,5,8,13,21,34,55,89,144
