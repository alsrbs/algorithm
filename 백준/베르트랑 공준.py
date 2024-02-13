import sys

input = sys.stdin.readline


a = [0, 0] + [1]*(246912)
for i in range(2, 246913):
    if a[i]:
        for j in range(2 * i, 246913, i):
            a[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    print(sum(a[n+1:n*2+1]))

