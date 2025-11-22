#day 10 operators (identity operators)


# Identity operators are used to compare the memory locations of two objects.
# The two main identity operators are:
# is
# is not

# is operator returns True if both variables point to the same object.
# is not operator returns True if both variables point to different objects.


# is operator example:

a = [1, 2, 3]
b = a
print("a is b :", a is b)  # True


# is not operator example:
c = [1, 2, 3]
print("a is not c :", a is not c)  # True


# Here are some examples to illustrate how identity operators work:
x = 10
y = 10
print("x is y :", x is y)  # True
print("x is not y :", x is not y)  # False

m = "hello"
n = "hello"
print("m is n :", m is n)  # True
print("m is not n :", m is not n)  # False
p = [4, 5, 6]
q = [4, 5, 6]
print("p is q :", p is q)  # False
print("p is not q :", p is not q)  # True


# You can also use identity operators with other data types:
num1 = 3.14
num2 = 3.14
print("num1 is num2 :", num1 is num2)  # True
print("num1 is not num2 :", num1 is not num2)  # False
char1 = 'A'
char2 = 'A'
