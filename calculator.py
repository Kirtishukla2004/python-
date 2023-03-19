
#using arthmetic operation
print("here's a calculator code in py")
a=int(input("enter first number "))
b=int(input("enter second number "))
choice=input("enter what you want to perform +,-,*,/,**,%  ")
if choice == '+' :
    print("her's your sum " + str(a+b))
elif choice == '-':
      print("her's your subtraction " + str(a-b))
elif choice == '*':
      print("her's your multiplication " + str(a*b))

elif choice == '/':
      print("her's your division " + str(a/b))
elif choice == '**':
      print("her's your power solved  " + str(a**b))
elif choice == '%':
      print("her's your  modulo " + str(a%b))
else:
      print("WRONG INPUTS .....")