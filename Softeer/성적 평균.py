import sys
input = sys.stdin.readline

n, k = map(int, input().split())
points = list(map(int, input().split()))

for _ in range(k):
    a, b = map(int, input().split())
    formatted_number = "{:.2f}".format(round(sum(points[a-1:b])/(b-a+1), 2))
    print(formatted_number)