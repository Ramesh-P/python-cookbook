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
