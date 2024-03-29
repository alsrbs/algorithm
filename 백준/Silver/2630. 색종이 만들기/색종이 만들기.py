import sys

input = sys.stdin.readline


def solution(x, y, N):
    color = arr[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != arr[i][j]:
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return

    result.append(color)
    
    
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = []
solution(0, 0, N)
print(result.count(0))
print(result.count(1))