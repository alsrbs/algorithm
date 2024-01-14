from itertools import combinations
N = int(input())
t_answer = dict(zip(input().split(), [i for i in range(N)]))
s_answer = list(combinations(list(input().split()), 2))
answer = 0
for p in s_answer:
    if t_answer.get(p[0]) < t_answer.get(p[1]):
        answer += 1
print(str(answer) + '/' + str((N*(N-1))//2))


