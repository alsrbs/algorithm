import sys
input = sys.stdin.readline

n, m = map(int, input().split())

for _ in range(m):
    k = int(input())
    arr = list(map(int, input().split()))

    for i in range(1, k):
        if arr[i-1] < arr[i]:
            print('No')
            exit()

print('Yes')