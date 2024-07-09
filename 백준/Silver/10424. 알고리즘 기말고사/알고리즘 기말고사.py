import sys
input = sys.stdin.readline

n = int(input())
ans = [0] * n
score = list(map(int, input().split()))

# 딕셔너리를 사용하여 값의 인덱스를 저장
score_index = {value: index + 1 for index, value in enumerate(score)}

for i in range(n):
    ans[i] = score_index[i + 1]
    print((i + 1) - ans[i])
