def rfact(n):
 if(n==0):
   return 1
 else:
   return n*rfact(n-1)
n=int(input("enter a positive number"))
r=rfact(n)
print("factorial of",n,"is",r)
