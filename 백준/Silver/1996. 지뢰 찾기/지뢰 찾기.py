import sys
input = sys.stdin.readline


def count(r, c):
    total = 0
    for i in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        nr = r + i[0]
        nc = c + i[1]

        if 0<= nr < n and 0<= nc < n and arr[nr][nc] != '.':
            total += int(arr[nr][nc])

    if total >= 10:
        answer[r][c] = 'M'
    else:
        answer[r][c] = str(total)


n = int(input())
arr = [list(input()) for _ in range(n)]
answer = [['*']*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if '.' == arr[i][j]:
            count(i, j)

for i in answer:
    print(''.join(i))