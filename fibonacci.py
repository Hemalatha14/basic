n=int(input("enter number for fibonacci series"))
x=0
y=1
print(x)
print(y)
count = 2
while(count<n):
      q=x+y
      x=y
      y=q
      print(q)
      count = count +1
      
