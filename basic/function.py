# Python 3.6.0
# No arguments, No return
def greet():
    print('Hello!')

greet()
# OUT: Hello!

# Python 3.6.0
# Single required argument, No return
def greet(name):
    print('Hi {}!'.format(name))

greet('Tom')
# OUT: Hi Tom!

# Python 3.6.0
# Many required arguments (ordered), No return
def greet(name, message):
    print('Welcome {}, {}!'.format(name, message))

greet('Tom', 'Good Morning')
# OUT: Welcome Tom, Good Morning!

# Python 3.6.0
# Keyword arguments (unordered), No return
def introduce(name, age):
    print('I am {}. I am {} years old'.format(name, age))

introduce(age = 12, name = 'Tom')
# OUT: I am Tom. I am 12 years old

# Python 3.6.0
# Default arguments, No return
def announce(month, year = '2017'):
    print('Today is 1st {}, {}'.format(month, year))

announce('April')
# OUT: Today is 1st April, 2017
announce('April', '2018')
# OUT: Today is 1st April, 2018

# Python 3.6.0
# Variable length arguments (undefined), No return
def items(fruit, *others):
    print(fruit)
    for item in others:
        print(item)

items('Apple')
# OUT: Apple
items('Apple', 'Orange', 'Mango')
# OUT: Apple, Orange, Mango

# Python 3.6.0
# Variable with global scope, No return
total = 0
def assign(number):
    total = number
    print('Value of local variable total is', total)

assign(10)
print('Value of global variable total is', total)
# OUT:
    # Value of local variable total is 10
    # Value of global variable total is 0

# Python 3.6.0
# Variable with global scope, With return
fruit = 'Apple'
def assign(name):
    fruit = name
    print('Value of local variable fruit is', fruit)
    return fruit

assign('Orange')
print('Value of global variable fruit is', fruit)
# OUT:
    # Value of local variable fruit is Orange
    # Value of global variable fruit is Apple

# Python 3.6.0
# Variable declared as global, No return
total = 0
print('Value of variable before the function call is', total)

def assign(number):
    global total
    total = number

assign(10)
print('Value of variable after the function call is', total)
# OUT:
    # Value of variable before the function call is 0
    # Value of variable after the function call is 10
