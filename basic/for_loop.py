# Python 3.6.0
# List of numbers
numbers = [0, 1, 2]
words = ['First', 'Second', 'Third']
for number in numbers:
    print('{} number is {}'.format(words[number], number))
# OUT:
    # First number is 0
    # Second number is 1
    # Third number is 2

# Python 3.6.0
# List of strings
toys = ['truck', 'marbles', 'ball']
for toy in toys:
    print(toy)
# OUT:
    # truck
    # marbles
    # ball

# Python 3.6.0
# Mixed list (numbers and strings)
collection = [1, 'book', 2, 'pens']
for item in collection:
    print(item)
# OUT:
    # 1
    # book
    # 2
    # pens

# Python 3.6.0
# List of lists
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in lists:
    print(list)
# OUT:
    # [1, 2, 3]
    # [4, 5, 6]
    # [7, 8, 9]

# Python 3.6.0
# String
for item in 'hello':
    print (item)
# OUT: h, e, l, l, o

# Python 3.6.0
# Range of all numbers
for number in range(10):
    print(number)
# OUT: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# Python 3.6.0
# Range of numbers between start and end
for number in range(3, 6):
    print(number)
# OUT: 3, 4, 5

# Python 3.6.0
# Range of numbers at equal step
for number in range(1, 10, 2):
    print(number)
# OUT: 1, 3, 5, 7, 9

# Python 3.6.0
# List of items by index
items = ['Rock', 'Paper', 'Scissors']
for index in range(len(items)):
    print(items[index])
# OUT:
    # Rock
    # Paper
    # Scissors

# Python 3.6.0
# Nested loops
units = [1, 2]
items = ['house', 'boat', 'car']
for unit in units:
    for item in items:
        print (unit, item)
# OUT:
    # 1 house
    # 1 boat
    # 1 car
    # 2 house
    # 2 boat
    # 2 car

# Python 3.6.0
# Exit
for number in range(10):
    if number == 3:
        break
    print(number)
# OUT: 0, 1, 2

# Python 3.6.0
# For...else
for number in range(3):
    print(number, 'is in range')
else:
    print(number + 1, 'is out of range')
# OUT:
    # 0 is in range
    # 1 is in range
    # 2 is in range
    # 3 is out of range
