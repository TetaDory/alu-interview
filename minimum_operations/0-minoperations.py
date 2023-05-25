import math

def minOperations(n):
    if n <= 1:
        return 0
    
    operation = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operation += divisor
        else:
            divisor += 1
    
    return operation
