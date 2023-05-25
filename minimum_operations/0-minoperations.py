import math

def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1
    
    return operations

# Example usage
n = 9
result = minOperations(n)
print("Number of operations:", result)
