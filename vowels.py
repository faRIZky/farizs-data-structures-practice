'''
- intialize vowels
- counter
- vowels saver
- return both
'''

def count_vowels(text):
    vowels = "AaIiUuEeOo"
    count = 0
    found_vowels = []

    for char in text:
        if char in vowels:
            count += 1
            found_vowels.append(char)
    return count, found_vowels

input_text = "Hello World"
vowels_count, vowels_list = count_vowels(input_text)
print(f"Number of vowels: {vowels_count}")
print(f"List of vowels found: {vowels_list}")

