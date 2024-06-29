import sys
input = sys.stdin.readline

n=318137
a = [False, False] + [True]*(n-1)
primes = []
ans = []
for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

super_prime = []
for i in range(len(primes)):
    if primes[i] <= 27449:
        super_prime.append(primes[primes[i] - 1])
    else:
        break

for _ in range(int(input())):
    num = int(input())
    print(super_prime[num-1])
