dic = {}
for i in range(8):
    score = int(input())
    dic[i+1] = score

total = 0
sort_lst = []
for k, v in sorted(dic.items(), key=lambda x:-x[1])[:5]:
    total += v
    sort_lst += [k]
print(total)
print(*sorted(sort_lst))