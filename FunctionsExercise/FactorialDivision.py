def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_division(a, b):
    first = factorial(a)
    second = factorial(b)
    return f"{first / second:.2f}"


num1 = int(input())
num2 = int(input())

print(factorial_division(num1, num2))
