#arthmetic operator 
def arthmetic(a,b):
    print("addition(+) "  + str(a+b)) #type conversion
    print("subtraction(-) "  + str(a-b)) #type conversion
    print("multiplication(*) "  + str(a*b)) #type conversion
    print("division(/) "  + str(a/b)) #type conversion
    print("modulo(%) "  + str(a%b)) #type conversion

def bitwise(a,b):
    print("here's the value of bitwise a and b " , str(a &  b ))
    
    print("here's the value of bitwise a and b " , str(a ^  b ))
    print("here's the value of bitwise a and b " , str(a>>2))


    print("here's the value of bitwise a and b " , str(a |  b ))

    print("here's the value of bitwise a and b " , str(b<<2 ))

    print("here's the value of bitwise a and b " , str(~a ))

def logial(marks):
      
       if marks <=90  and  marks >=80 :
            print(" A GRADE ...")
       elif marks <=80 and marks >=70 :
             print("B grade ......")
             
       elif marks <=70  and  marks >=60 :
            print(" C GRADE ...")
       elif marks <=60 and marks >=50 :
             print(" D GRADE.....")
       else:
            print("PASSED....")
        
def  special(str):
     if str is 'a':
          print("position of  a is " ,str.find('a'))
     elif str is not 'a':
          print("there is no a exists....")
      
     

arthmetic(2,5)
bitwise(10,4)
logial(9)
special('aman')
list =[]
for i in range(0,5):
     ele=int(input())
     list.append(ele)


print(list)
print(list[:])
list1=['maths',98],['science',99]
print(list1)

       
          
    
