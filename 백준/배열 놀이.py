import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())    # 배열의 길이, 연산의 횟수
    arr = [list(map(int, input().split())) for _ in range(N)]   # 2차 배열

    row_sums = [sum(row) for row in arr]
    col_sums = [sum(col) for col in zip(*arr)]

    # 연산
    for _ in range(M):
        r1, c1, r2, c2, v = map(int, input().split())

        for i in range(c1-1, c2):
            col_sums[i] += (r2-r1+1)*v
        for i in range(r1-1, r2):
            row_sums[i] += (c2-c1+1)*v

    print(*row_sums)
    print(*col_sums)

