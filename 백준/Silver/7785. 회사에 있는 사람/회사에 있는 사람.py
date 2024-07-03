import sys
input = sys.stdin.readline

n = int(input())
ans = set()
for i in range(n):
    log = input().split()

    if log[1] == 'enter':
        ans.add(log[0])
    else:
        ans.discard(log[0])

for i in sorted(ans, reverse=True):
    print(i)