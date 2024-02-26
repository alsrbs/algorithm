n, left, right = map(int, input().split())
answer = []

for i in range(left, right+1):
    answer.append(max(i//n, i%n) + 1)

print(answer)
