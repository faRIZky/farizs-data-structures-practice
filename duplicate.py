numbers = [3, 5, 2, 9, 1, 5, 9, 6, 9]
counts = {}
duplicates = []

for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

print(counts)

duplicates1 = [num for num, count in counts.items() if count > 2]
print(f"dumpicates1 : {duplicates1}")

# find numbers has more than 1 count --> append()
for num, count in counts.items():
    if count > 1:
        duplicates.append(num)

print(duplicates)
'''
or 
# Find numbers with counts greater than 1 (duplicates)

duplicates = [num for num, count in counts.items() if count > 1]
print("Duplicates:", duplicates)  # Output: [5, 9]
'''

