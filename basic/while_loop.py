# Python 3.6.0
# While loop
i = 1
count = 10
sum = 0
while i <= count:
    sum = sum + i
    print(sum)
    i = i + 1
print('The total is', sum)
# OUT:
    # 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
    # The total is 55

# Python 3.6.0
# While...else loop
i = 1
count = 10
sum = 0
while i <= count:
    sum = sum + i
    print(sum)
    i = i + 1
else:
    print('The total is', sum)
# OUT:
    # 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
    # The total is 55
