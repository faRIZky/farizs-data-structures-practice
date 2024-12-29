def odd_even (num):
    even = []
    odd = []
    for number in num:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return odd, even


array1 = [1, 5, 3, 2, 4, 8]
odd_array, even_array = odd_even(array1)
print(f"odd: {odd_array} , even: {even_array}")
