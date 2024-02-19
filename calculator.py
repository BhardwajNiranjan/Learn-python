num1=int(input("enter first value:- "))
num2=int(input("enter second value:- "))

operator=input("enter operators........")

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":    
    print(num1*num2)
elif operator=="/":    
    print(num1/num2)
elif operator=="%":    
    print(num1%num2)
else:
    print("invalid operator....")