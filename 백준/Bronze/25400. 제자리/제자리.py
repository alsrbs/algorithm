n = int(input())
arr = list(map(int, input().split()))
answer = 0
for i in range(n):
    if answer + 1 == arr[i]:
        answer += 1
print(n - answer)
