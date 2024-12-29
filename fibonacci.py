'''

the first two elements will be 1 or 0 or whatever
and for the next element will be THE SUM OF TWO NUMBERS before

Fn = F(n-1) + F(n-2)

- intialise the first two numbers
- loop from the third to nth element --> specify n outside the function
- calulate next element --> [index -1] - [index -2]
- append it to sequence

- input the length of sequence (n)
- input the first and second (optional)
- print result

'''

def fibonacci (n, first= 0, second = 1):
    sequence = [first, second]
    for _ in range (2, n):
        next_number = sequence [-1] + sequence [-2]
        sequence.append(next_number)
    return sequence

user_input = 10
result = fibonacci(user_input, 0, 1)

print(result)


