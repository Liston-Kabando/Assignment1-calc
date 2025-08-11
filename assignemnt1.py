num_1=float(input("enter first number"))
num_2=float(input("enter second number"))
operation=(input("enter operation(+,-,*,/):"))

if operation=="+":
    result=num_1+num_2
if operation=="-":
    result=num_1-num_2
if operation=="*":
    result=num_1*num_2
if operation=="/":
    result=num_1/num_2
    if num_2 !=0:
        result=num_1/num_2
    else:
        result="error:Division by zero is not allowed"
else:
    result="invalid operation" 
print(f"{num_1}{operation}{num_2}={result}") 
