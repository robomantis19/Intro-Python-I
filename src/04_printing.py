"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

#printf('x is %s, y is %s, z is \"I like turtles!\"', 10,2.24552 );

# Use the 'format' string method to print the same 
string = f'x is {x}, y is {y}, z is \"I like turtles!\"'
print(string.format(str(x), str(y)))

##---------------------------------------------*******-----*******--------

# Finally, print the same thing using an f-string

print(string)