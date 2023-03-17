# Check Prime Number
import math
import random


def isPrime(n):
    print("n = ", n)
    sqrtN = int(math.sqrt(n))
    for i in range(2, sqrtN):
        if n % i == 0:
            print("i = ", i)
            return "n is not prime"
    return "n is prime"


print(isPrime(random.randrange(2, 32768)))
