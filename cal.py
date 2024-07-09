#num1= input("enter a number: ")
#num2= input("enter a number: ")
#res= float(num1)+float(num2)
#print(res)
num= float(input("enter the number: "))
op= input("enter operator: ")
num1= float(input("enter the 2nd number: "))
if op == "+":
    print(num+num1)
elif op == "-":
    print(num-num1)
elif op == "*":
    print(num*num1)
elif op == "/":
    print(num/num1)
else:
    print("invalid operator")
   
