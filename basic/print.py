# Python 3.6.0
# Print some text
print('Hello World!')
# OUT: Hello World!

# Python 3.6.0
# Print some text (alternate syntax)
print("Hello World!")
# OUT: Hello World!

# Python 3.6.0
# Print variable
a = 10
print(a)
# OUT: 10

# Python 3.6.0
# Print text and variable
a = 10
print('The value of a is', a)
# OUT: The value of a is 10

# Python 3.6.0
# Print text and variable
age = 'He is %d years old' % 10
print(age)
# OUT: He is 10 years old

# Python 3.6.0
# Print formatted text and variable
cost = 'The cost is $%.2f' % 10
print(cost)
# OUT: The cost is $10.00

# Python 3.6.0
# Print two variables
name = 'Tom'
greeting = 'Good Morning'
print(greeting,',', name,'!')
# OUT: Good Morning , Tom !

# Python 3.6.0
# Print two variables w/o white space
name = 'Tom'
greeting = 'Good Morning'
print(greeting, name, sep=', ', end='!')
# OUT: Good Morning, Tom!

# Python 3.6.0
# Print with output formatting
a = 5
b= 10
print('The value of a is {} and b is {}'.format(a, b))
# OUT: The value of a is 5 and b is 10

# Python 3.6.0
# Print ordered output
this = 'butter'
that = 'bread'
print('I like {1} and {0}'.format(this, that))
# OUT: I like bread and butter

# Python 3.6.0
# Print using keyword
print('Hi {name}, {greeting}!'.format(name = 'Tom', greeting = 'Good Morning'))
# OUT: Hi Tom, Good Morning!


# Python 2
print 1, 2, 3
# 1 2 3
print 1
# 1
print 1,
# 1 (no trailing newline)

# Python 3
print(1, 2, 3)
# 123
print(1, 2, 3, sep = " ")
# 1 2 3
print(1)
# 1
print(1, end = "")
# 1 (no trailing newline)
