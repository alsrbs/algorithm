n1, m1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n1)]
n2, m2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n2)]

answer = [[0] * m2 for _ in range(n1)]

for i in range(n1):
    for j in range(m2):
        for k in range(m1):
            answer[i][j] += a[i][k] * b[k][j]

for row in answer:
    print(*row)