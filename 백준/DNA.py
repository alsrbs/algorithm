N, M = map(int, input().split())
d = {}
for i in range(M):
    d[i] = {}

for i in range(N):
    word = input()

    for j in range(M):
        if word[j] in d[j]:
            d[j][word[j]] += 1
        else:
            d[j][word[j]] = 1

st = ''
cnt = 0
for i in range(M):
    sorted_dict = sorted(d[i].items(), key=lambda item: (-item[1], item[0]))
    st += sorted_dict[0][0]
    cnt += N - sorted_dict[0][1]
print(st)
print(cnt)