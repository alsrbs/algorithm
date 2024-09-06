import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = [0, 0]  # 학번, 같은 반이었던 학생 수

for i in range(n):
    cnt = set()
    for j in range(5):  # 5개의 학년, 각 학년에 대해 확인
        for k in range(n):
            if arr[i][j] == arr[k][j]:
                cnt.add(k)

    # 같은 반이었던 학생 수가 더 많은 경우 업데이트
    if answer[1] < len(cnt):
        answer[1] = len(cnt)
        answer[0] = i+1

print(answer[0])