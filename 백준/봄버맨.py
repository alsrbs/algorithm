import sys

input = sys.stdin.readline


def explode():
    for r in range(R):
        for c in range(C):
            if graph[r][c] == 'O':
                bombs1[r][c] = '.'
            else:
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= r + i < R and 0 <= c + j < C and graph[r + i][c + j] == 'O':
                        bombs1[r][c] = '.'
                        break

    for r in range(R):
        for c in range(C):
            if bombs1[r][c] == 'O':
                bombs2[r][c] = '.'
            else:
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= r + i < R and 0 <= c + j < C and bombs1[r + i][c + j] == 'O':
                        bombs2[r][c] = '.'
                        break


R, C, N = map(int, input().split())
graph = [input().replace('\n', '') for _ in range(R)]

bombs = []
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'O':
            bombs.append((i, j))

if N == 1:
    for i in graph:
        print(''.join(i))

elif N % 4 == 2 or N % 4 == 0:
    for i in range(R):
        print('O'*C)

else:
    bombs1 = [['O'] * C for i in range(R)]
    bombs2 = [['O'] * C for i in range(R)]
    explode()

    if N % 4 == 1:
        for i in bombs2:
            print(''.join(i))
    if N % 4 == 3:
        for i in bombs1:
            print(''.join(i))

