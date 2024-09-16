import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    words = [input().strip() for _ in range(n)]
    print(sorted(words, key=str.lower)[0])
