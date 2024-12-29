numbers = [3, 5, 2, 9, 1, 5, 9, 6]

min_value = min(numbers)
max_value = max(numbers)

print(max_value)
print(min_value)

# Finding max manually (alternative approach)
manual_max = numbers[0]

for number in numbers[1:]:  # Start from the second element
    if number > manual_max:
        manual_max = number

print("Manual Max:", manual_max)

manual_min = numbers[0]

for number in numbers[1:]:
    if (number < manual_min):
        manual_min = number
print("Manual Min: ", manual_min)
'''
pen ngulang extends aja siii,,, since we're doing some list thingy right now . . .

numbers1 = [3, 5, 2, 9, 5, 2, 9, 6]
print(numbers1)                         # [3, 5, 2, 9, 5, 2, 9, 6]

numbers2 = [2, 9, 2, 3, 1, 4, 8, 10]

numbers1_non_extended = numbers1
print(numbers1_non_extended)            # [3, 5, 2, 9, 5, 2, 9, 6]


numbers1.extend(numbers2)
print(numbers1)                         # [3, 5, 2, 9, 5, 2, 9, 6, 2, 9, 2, 3, 1, 4, 8, 10]
'''

