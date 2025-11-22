#day 9 operators (logical operators)


# it returns boolean value(True or False)



# Logical operators are used to combine conditional statements.
# The three main logical operators are:
# and
# or
# not

#and operator returns True if both statements are true.
#or operator returns True if one of the statements is true.
#not operator reverses the result, returns False if the result is true.

#and operator example:



a = 10
b = 5
print("a > 5 and b < 10 :", a > 5 and b < 10)  # True
print("a > 15 or b < 10 :", a > 15 or b < 10)  # True
print("not(a > 5) :", not(a > 5))  # False

# Here are some examples to illustrate how logical operators work:

x = 7
y = 3
print("x > 5 and y < 5 :", x > 5 and y < 5)  # True
print("x < 5 or y < 5  :", x < 5 or y < 5)   # True
print("not(x < 5)       :", not(x < 5))       # True
# You can also combine multiple logical operators in a single expression:


age = 20    
is_student = True
print("age > 18 and is_student == True :", age > 18 and is_student == True)  # True

