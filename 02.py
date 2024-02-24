def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numbers = [5, 7, 10, 3, 6]

factorial_results = [str(factorial(num)) for num in numbers]

print(','.join(factorial_results))
