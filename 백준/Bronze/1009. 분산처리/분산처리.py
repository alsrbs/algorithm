import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a = a % 10

    if a == 0:
        print(10)
    elif a in [1, 5, 6]:
        print(a)
    elif a in [4, 9]:
        print(a if b % 2 else a**2 % 10)
    else:
        print(a**(b % 4) % 10 if b % 4 else a**4 % 10)
