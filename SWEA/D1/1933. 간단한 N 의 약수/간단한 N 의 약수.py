n = int(input())
answer = []
for i in range(1, int(n**1/2)):
    if n%i == 0:
        answer += [i, n//i]
print(*sorted(set(answer)))