#day 7 operators (assignment operators)



#2. Assignment Operators

# Assignment operators are used to assign values to variables.

# They are used to assign the result of an operation to a variable. 

# Here is the list of assignment operators:


    # "=" : Assigns the value on the right to the variable on the left.
    # "+=" : Adds the value on the right to the variable on the left and assigns the result to the variable on the left.
    # "-=" : Subtracts the value on the right from the variable on the left and assigns the result to the variable on the left.
    # "*=" : Multiplies the variable on the left by the value on the right and assigns the result to the variable on the left.
    # "/=" : Divides the variable on the left by the value on the right and assigns the result to the variable on the left.
    # "%=" : Takes the modulus of the variable on the left by the value on the right and assigns the result to the variable on the left.
    # "**=" : Raises the variable on the left to the power of the value on the right and assigns the result to the variable on the left.
    # "//=" : Performs floor division on the variable on the left by the value on the right and assigns the result to the variable on the left.

# Here are some examples of assignment operators:


a = 10
b = 3
a += b  # a = a + b

print("After += :", a)  # After += : 13
a -= b  # a = a - b
print("After -= :", a)  # After -= : 10
a *= b  # a = a * b
print("After *= :", a)  # After *= : 30
a /= b  # a = a / b
print("After /= :", a)  # After /= : 10.0
a %= b  # a = a % b
print("After %= :", a)  # After %= : 1.0
a **= b  # a = a ** b
print("After **= :", a)  # After **= : 1000.0
a //= b  # a = a // b
print("After //= :", a)  # After //= : 333.0


# operator precedence:

# operator precedence determines the order in which operations are performed in an expression.

# here is the operator precedence list from highest to lowest:

# 1. Parentheses ()
# 2. Exponentiation (**)
# 3. Multiplication (*), Division (/), Floor Division (//), and Modulus
# 4. Addition (+) and Subtraction (-)

# here is some example of operator precedence:

x = 5
y = 6
z = 2

print(x + y * z)          # 17  (multiplication first, then addition)
print((x + y) * z)       # 22  (parentheses first, then multiplication)
print(x ** y + z)       # 3125 (exponentiation first, then addition)
print(x + y - z)       # 9   (addition first, then subtraction)
print(x + y / z)      # 8.0 (division first, then addition)
print(x // z + y)     # 8   (floor division first, then addition)       

# now you have learned about assignment operators and operator precedence.
# assignment operators are very useful in programming as they help to simplify code and make it more readable.

# Assigning an integer value
age = 30

# Assigning a string value
name = "Alice"

x = 10  # Initial value

# Addition assignment
# x += 5 is the same as x = x + 5
x += 5
print(f"After += 5, x is: {x}") # Output: 15

# Subtraction assignment
# x -= 3 is the same as x = x - 3
x -= 3
print(f"After -= 3, x is: {x}") # Output: 12

# Multiplication assignment
# x *= 2 is the same as x = x * 2
x *= 2
print(f"After *= 2, x is: {x}") # Output: 24

# Division assignment (results in a float)
# x /= 4 is the same as x = x / 4
x /= 4
print(f"After /= 4, x is: {x}") # Output: 6.0

# Modulus assignment (finds the remainder after division)
# x %= 5 is the same as x = x % 5
x %= 5
print(f"After %= 5, x is: {x}") # Output: 1.0

# Floor division assignment (discards the fractional part)
# x //= 1 is the same as x = x // 1
x //= 1
print(f"After //= 1, x is: {x}") # Output: 1.0

# Exponentiation assignment (power of)
# x **= 3 is the same as x = x ** 3
x **= 3
print(f"After **= 3, x is: {x}") # Output: 1.0

a = 5  # Binary: 0101

# Bitwise AND assignment
# a &= 3 is the same as a = a & 3 (0101 & 0011 = 0001)
a &= 3
print(f"After &= 3, a is: {a}") # Output: 1

# Bitwise OR assignment
# a |= 2 is the same as a = a | 2 (0001 | 0010 = 0011)
a |= 2
print(f"After |= 2, a is: {a}") # Output: 3

# Left shift assignment
# a <<= 1 is the same as a = a << 1 (0011 << 1 = 0110)
a <<= 1
print(f"After <<= 1, a is: {a}") # Output: 6
