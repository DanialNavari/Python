#Import Math Library
import math

#Select Operator
print("Select Operator")
print("+ : sum")
print("- : sub")
print("* : mul")
print("/ : div")
print("sin")
print("cos")
print("tan")
print("cotan")
print("sqrt")
print("factorial")

#Give Operator
op = input("Enter Operator: ")

#List of Operators
op_list_two_arg = ["+","-","*","/"]
op_list_one_arg = ["sin","cos","tan","cot"]
op_list_other = ["sqrt","factorial"]

#Conditions
if op in op_list_two_arg:
    #Give "a" & "b" 
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))

    if op=='+':
        result = a + b
    elif op=='-':
        result = a - b
    elif op=="*" :
        result = a * b
    elif op=="/":
        if b==0:
            result = "Not a Number"
        else:
            result = a / b
    
elif op in op_list_one_arg:

    #Give "a" & Convert degree to radian
    a = float(input("Enter First Number: "))
    rad = math.radians(a)

    if op=='sin':
        result = math.sin(rad)
    if op=='cos':
        result = math.cos(rad)
    if op=='tan':
        result = math.tan(rad)
    if op=='cot':
        result = 1/math.tan(rad)

elif op in op_list_other:
    
    if op=="factorial":
        #Give "a" 
        a = int(input("Enter First Number: "))
        result = math.factorial(a)
    elif op=="sqrt":
        #Give "a" 
        a = float(input("Enter First Number: "))
        result = math.sqrt(a)

print(result)


