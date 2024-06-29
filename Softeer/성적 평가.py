n = int(input())
total_score = [0]*n
for _ in range(3):
    score = list(map(int, input().split()))
    score_sort = sorted(score, reverse=True)

    # 점수별 등수
    rank = {}
    for i in range(n):
        total_score[i] += score[i]
        if score_sort[i] not in rank:
            rank[score_sort[i]] = i+1

    # 등수 적용
    ans = []
    for i in score:
        ans.append(rank[i])
    print(*ans)

# 최종등수
total_score_sort = sorted(total_score, reverse=True)
total_rank = {}
for i in range(n):
    if total_score_sort[i] not in total_rank:
        total_rank[total_score_sort[i]] = i+1

ans = []
for i in total_score:
    ans.append(total_rank[i])
print(*ans)
