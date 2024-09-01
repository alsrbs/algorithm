n = int(input())
peaks = list(map(int, input().split()))

answer = 0
h = 0
cnt = 0
for i in range(n):
    if h > peaks[i]:
        cnt += 1
    else:
        h = peaks[i]
        answer = max(cnt, answer)
        cnt = 0
else:
    answer = max(cnt, answer)
    
print(answer)