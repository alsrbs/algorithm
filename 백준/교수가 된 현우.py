import sys

input = sys.stdin.readline

def count_zeros_in_factorial(N):
    count, power_of_5 = 0, 5

    while N // power_of_5 > 0:
        count += N // power_of_5
        power_of_5 *= 5

    return count

t = int(input())
for _ in range(t):
    print(count_zeros_in_factorial(int(input())))
