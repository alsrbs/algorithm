import sys, heapq

input = sys.stdin.readline


n, m, k = map(int, input().split())
beer = [list(map(int, input().split())) for _ in range(k)]
beer = sorted(beer, key=lambda x: (x[1], x[0]))

result = []
preference = 0
answer = -1

for i in beer:
    x1, x2 = i
    preference += x1
    heapq.heappush(result, x1)

    if len(result) == n:
        if preference >= m:
            answer = x2
            break
        else:
            preference -= heapq.heappop(result)

print(answer)
