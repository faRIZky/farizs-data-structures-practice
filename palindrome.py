'''
palindrome is a terms of a word that being the same as the reversed one

for example:
the word of "KAYAK" is  palindrome because the word remind the same as the reversed one.

another example is the word of madam

steps:
- define a function to  check if the word that being passed is a palindrome or not
- change the word to lowercase
- reversed the word
- check if it remains the same or not
- display the result
'''

# Define the function
def isPalindrome (s):
    s_lower = s.lower()
    if (s_lower == s[::-1]):
        return f"{s} is a palindrome"
    else:
        return f"{s} is not a palindrome"

user_input = input("Enter string: ")
print(isPalindrome(user_input))


'''
remember python slicing

start:step:stop

cek aja file slicing.py
'''


'''
palindrom is the terms of when the string is remains the same after they're being reversed.

for example, "MADAM", "KAYAK", etc.

- convert all the alphabet into lowercase
- reversed the string
- check if the string still remains the same or not
- display the result
'''

def isPalindrome2 (text):
    text = text.lower()
    reversed_text = text[::-1]
    if text == reversed_text :
        print(f"{text} is a palindrome")
    else:
        print(f"{text} is not a palindrome")

user_input = "KAYAK"
isPalindrome2(user_input)