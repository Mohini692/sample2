def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
  
number = 5
print(f"Factorial of {number} (Iterative):", factorial_iterative(number))
