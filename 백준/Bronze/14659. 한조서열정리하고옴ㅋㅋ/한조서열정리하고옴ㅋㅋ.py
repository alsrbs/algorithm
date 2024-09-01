n = int(input())
peaks = list(map(int, input().split()))

answer = 0
x = 0
for i in range(n-1):
    cnt = 0
    for j in range(i+1, n):
        if peaks[i] > peaks[j]:
            cnt += 1
        else:
            x = j
            break

    answer = max(cnt, answer)

    if x + answer >= n:
        break

print(answer)