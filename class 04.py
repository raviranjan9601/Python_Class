#day 8 Operators (Comparison Operators)


#3. Comparison Operators 
# Comparison operators are used to compare two values.
# They return a boolean value (True or False) based on the comparison.

# Here is the list of comparison operators:

    # "==" : Equal to
    # "!=" : Not equal to
    # ">"  : Greater than
    # "<"  : Less than
    # ">=" : Greater than or equal to
    # "<=" : Less than or equal to



# Here are some examples of comparison operators:


x = 10
y = 5

print("x == y :", x == y)  # x == y : False
print("x != y :", x != y)  # x != y : True
print("x > y  :", x > y)   # x > y  : True
print("x < y  :", x < y)   # x < y  : False
print("x >= y :", x >= y)  # x >= y : True
print("x <= y :", x <= y)  # x <= y : False


# now you have learned about comparison operators.
# comparison operators are very useful in programming as they help to make decisions based on conditions.
# Here are some examples of variable assignments using different data types:

# Assigning a float value
height = 5.9

# Assigning a boolean value
is_student = True

# Assigning a list
fruits = ["apple", "banana", "cherry"]

# Assigning a dictionary
person = {"name": "Bob", "age": 25}
# Assigning a tuple
coordinates = (10.0, 20.0)
# Assigning a set
unique_numbers = {1, 2, 3, 4, 5}


# You can use comparison operators to compare these variables as well.

print("age > 18 :", age > 18)  # age > 18 : True
print("height < 6.0 :", height < 6.0)  # height < 6.0 : True
print("is_student == True :", is_student == True)  # is_student == True : True
print("len(fruits) != 0 :", len(fruits) != 0)  # len(fruits) != 0 : True
print("person['age'] >= 21 :", person['age'] >= 21) # person['age'] >= 21 : True
print("coordinates[0] <= 10.0 :", coordinates[0] <= 10.0)  # coordinates[0] <= 10.0 : True
print("3 in unique_numbers :", 3 in unique_numbers)  # 3 in unique_numbers : True

# You can also combine comparison operators with logical operators to create more complex conditions.

is_adult = (age >= 18) and (is_student == False)
print("is_adult :", is_adult)  # is_adult : True


# Here, we check if age is greater than or equal to 18 and if is_student is False.
# The result is stored in the variable is_adult.
# now you have learned about variable assignments using different data types and how to use comparison operators with them.

x += 5  # x = x + 5
print("After += :", x)  # After += : 15


