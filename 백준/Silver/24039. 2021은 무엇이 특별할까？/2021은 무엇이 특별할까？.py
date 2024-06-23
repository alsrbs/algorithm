n=10000
a = [False,False] + [True]*(n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

N = int(input())

ans = set()
for i in range(len(primes)-1):
    num = primes[i]*primes[i+1]
    if N < num:
        ans.add(num)
        if num >= 10000:
            break

print(sorted(ans)[0])