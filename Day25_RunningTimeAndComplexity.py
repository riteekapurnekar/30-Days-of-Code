from math import sqrt

test_cases = int(input())

def isPrime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i is 0:
            return False
    return True


for j in range(test_cases):
    n = int(input())
    
    if n >= 2 and isPrime(n):
        print("Prime")
    else:
        print("Not prime")
