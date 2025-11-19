#day 6 operators

#An operator is a symbol or keyword that tells the computer what operation it should perform on values or variables.

#operators has seven types:
#1.arithmetic operators
#2.assignment operators
#3.comparison operators
#4.logical operators
#5.identity operators
#6.membership operators
#7.bitwise operators

#today we will learn about arithmetic operators.
"""arthmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, and division."""
#here is the list of arthmetic operators:
# "+ " : add
# "- " : subtract
# "* " : multiply
# "/ " : divide
# "% " : modulus
# "** " : exponentiation
# "// " : floor division
# here is some example of arthmetic operators:
a=10
b=3
print("Addition:",a+b)          # Addition: 13 
print("Subtraction:",a-b)       # Subtraction: 7
print("Multiplication:",a*b)    # Multiplication: 30
print("Division:",a/b)          # Division: 3.333333333333333
print("Modulus:",a%b)           # Modulus: 1
print("Exponentiation:",a**b)   # Exponentiation: 1000
print("Floor Division:",a//b)   # Floor Division: 3

#addition give us added value
#subtraction give us subtracted value
#multiplication give us multiplied value
#division give us Quotient value 
#modulus give us remainder value
#exponentiation give us power value
#floor division give us Quotient value without decimal point.

# operator precedence:
# operator precedence determines the order in which operations are performed in an expression.
# here is the operator precedence list from highest to lowest:
#1. Parentheses ()
#2. Exponentiation (**)
#3. Multiplication (*) and Division (/) and Floor Division (//) and Modulus (%)
#4. Addition (+) and Subtraction (-)
# here is some example of operator precedence:
x=5
y=6
z=2
print(x+y*z)          # 17  (multiplication first, then addition)   
print((x+y)*z)       # 22  (parentheses first, then multiplication)
print(x**y+z)       # 3125 (exponentiation first, then addition)
print(x+y-z)       # 9   (addition first, then subtraction)
print(x+y/z)      # 5.0 (division first, then addition)
print(x//z+y)     # 8   (floor division first, then addition)
# now you have learned about arthmetic operators and operator precedence.
# practice time:
#1. Write a program to calculate the area of a rectangle using arthmetic operators.
length=10
breadth=5
area=length*breadth
print("Area of rectangle:",area)   # Area of rectangle: 50
#2. Write a program to calculate the perimeter of a rectangle using arthmetic operators.
perimeter=2*(length+breadth)
print("Perimeter of rectangle:",perimeter)   # Perimeter of rectangle: 30
#3. Write a program to calculate the average of three numbers using arthmetic operators.
num1=10
num2=20
num3=30
average=(num1+num2+num3)/3
print("Average of three numbers:",average)   # Average of three numbers: 20.
#4. Write a program to calculate the simple interest using arthmetic operators.
principal=1000
rate=5
time=2
simple_interest=(principal*rate*time)/100
print("Simple Interest:",simple_interest)   # Simple Interest: 100.0
#5. Write a program to calculate the compound interest using arthmetic operators.
compound_interest=principal*(1+rate/100)**time - principal
print("Compound Interest:",compound_interest)   # Compound Interest: 102.5