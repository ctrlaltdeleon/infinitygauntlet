def isPrime(n):
    for index in range(2, n):
        if n % index == 0:
            return False
    return True


n = int(input())
print(isPrime(n))
