def fizzbuzz (n):
    for number in range(1, n+1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")

user_input = input("Enter number: ")
fizzbuzz(int(user_input))


'''
Why FizzBuzz is Placed First in the Logic???

When a number is divisible by both 3 and 5, we want "FizzBuzz". 
So, we have to check for this case first to avoid missing it. 

If we place the conditions for "Fizz" and "Buzz" first, they’ll trigger 
when the number is a multiple of 3 or 5 alone and skip the "FizzBuzz" check.

'''