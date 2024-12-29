'''
- count occurane
- find max count in count.values()

'''

numbers = [3, 5, 2, 9, 1, 5, 9, 6, 9, 3, 3]
counts = {}

# count occurance
for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
print(counts)

max_count = 0

for count in counts.values():
    if max_count < count:
        max_count = count
print(max_count)

majority=[num for num, count in counts.items() if count == max_count]
print(f"{majority} with count : {max_count}")