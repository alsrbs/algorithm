def Fibonacci_numbers(a, b, n):
    if n == 0:
        return a
    else:
        x = a + b
        return Fibonacci_numbers(b, x, n - 1)

n = int(input())
print(Fibonacci_numbers(0, 1, n))

