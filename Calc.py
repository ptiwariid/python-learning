from audioop import add
from wsgiref.validate import InputWrapper
import math
print("Input one of operand to run ---- add,sub,mul,div")
opr = input("Input Operation ")
a = int(input("first value "))
b = int(input("second value "))
c=a + b
d=a - b 
e=a * b
if opr == "add" :
    print("Addition",c)
if opr == "sub" :
    print("Sub",d)
if opr == "mul" :
    print("Mul",e)
if opr == "div" :
    print ("div",a / b)
if opr == "sqrt" :
    digit = int(input("enter digit"))
    print(math.sqrt(digit))