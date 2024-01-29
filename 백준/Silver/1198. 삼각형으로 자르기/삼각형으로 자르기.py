from itertools import combinations


# 삼각형의 넓이 계산
def triangle(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
    return area

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
combi = list(combinations(points, 3))
result = 0

for i in combi:
    x1, y1 = i[0]
    x2, y2 = i[1]
    x3, y3 = i[2]

    area = triangle(x1, y1, x2, y2, x3, y3)
    result = max(area, result)

print(result)
