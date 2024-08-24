n = int(input())
t = sorted(map(int, input().split()), reverse=True)

day = 1 + n
for i in range(n):
    t[i] -= n - i - 1

day += max(t)
print(day)
