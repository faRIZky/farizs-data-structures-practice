# SQUARES
squares = [x**2 for x in range(5)]
print(squares)

# EXTEND LIST
list1 = [1,2,3,4,5]
list1.append(6)

print(list1)

list2 = [10, 11, 12]
list1.extend(list2)
print(list2)

# LAMBDA
multiple = lambda x, y: x*y
result = multiple(3, 5)
print(result)

divider = lambda x, y : x/y
result1 = divider(2, 4)
print(result1)

# REVERSE LIST
initial_list = [1, 2, 3, 4, 5]
reversed_list = initial_list[::-1]
print(reversed_list)
