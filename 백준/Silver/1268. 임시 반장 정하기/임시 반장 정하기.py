n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = [0]*n

for i in range(n):
    cnt = set()
    for j in range(5):  # 5개의 학년, 각 학년에 대해 확인
        for k in range(n):
            if arr[i][j] == arr[k][j]:
                cnt.add(k)

    answer[i] = len(cnt)

print(answer.index(max(answer))+1)