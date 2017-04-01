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
