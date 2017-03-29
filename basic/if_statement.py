# Python 3.6.0
# If statement
a = 5
if a > 0:
    print('{} is greater than 0'.format(a))
# OUT: 5 is greater than 0

# Python 3.6.0
# If...Else statement
a = -5
if a > 0:
    print('{} is greater than 0'.format(a))
else:
    print('{} is less than 0'.format(a))
# OUT: -5 is less than 0

# Python 3.6.0
# If...Elif...Else statement
a = 0
if a > 0:
    print('{} is greater than 0'.format(a))
elif a == 0:
    print('zero')
else:
    print('{} is less than 0'.format(a))
# OUT: zero

# Python 3.6.0
# Nested If statement
a = 5
if a >= 0:
    if a == 0:
        print('zero')
    else:
        print('{} is greater than 0'.format(a))
else:
    print('{} is less than 0'.format(a))
# OUT: 5 is greater than 0
