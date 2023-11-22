N, M = map(int, input().split())
list_P = []
for i in range(M):
    list_P += [int(input())]
list_P.sort()
d = {}
if M <= N:
    for i in range(M):
        d[list_P[i] * (M - i)] = list_P[i]
    print(d[max(d)], max(d))
else:
    for i in range(N):
        d[list_P[abs(M-N):][i] * (N - i)] = list_P[abs(M-N):][i]
    print(d[max(d)], max(d))