N = int(input())
mountains = list(map(int, input().split()))

result = 0
for i in range(1, len(mountains)):
    result += (mountains[i-1] + mountains[i])**2 + abs(mountains[i-1] - mountains[i])**2

print(result)