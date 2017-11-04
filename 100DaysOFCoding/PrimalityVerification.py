# to check whether a no is prime or not
# Sieve of Eratosthenes https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def isprime(n):
    if n <= 1:
        return n, ' is prime'
    i = 2
    while i * i <= n:
        if n % i == 0:
            return n, ' is divisible', i
        i = i + 1
    return n, 'is prime'


print(isprime(25503111))
print(isprime(253111))
print(isprime(1))
print(isprime(0))
print(isprime(2))