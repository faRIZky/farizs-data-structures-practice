'''
number that is greater than 1 and only resulted 0 if and only if divided by itself.

to check if n is prime, you need to test for factors up to sqrt(n).
if there is any factor, then it's not a prime number.

check if the number is > 1
faktorisasi dari 2 sampe sqrt(n)
return true or false


generate:
dari hasil true itu masukin di append di sebuah list
'''

def isPrime(n):
    if n <= 1:
        return False
    for i in range (2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generatePrime (limit):
    primes = []
    for num in range (2, limit + 1):
        if isPrime(num):
            primes.append(num)
    return primes


print(isPrime(29))
print(generatePrime(50))

