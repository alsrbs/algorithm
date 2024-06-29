import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s, t = input().upper().split()
    print(t[s.index('X')], end='')

