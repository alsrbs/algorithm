def solution(friends, gifts):
    give = {}
    receive = {}
    result = {}
    for i in friends:
        receive.setdefault(i, [])
        receive.setdefault(i, [])
        give.setdefault(i, [])
        give.setdefault(i, [])
        result.setdefault(i, 0)
        
    for i in gifts:
        a, b = i.split()

        give[a].append(b)
        receive[b].append(a)


    for i in friends:
        c = 0
        for j in friends:
            if i == j:continue

            if j in give[i] or i in give[j]:
                if give[i].count(j) > give[j].count(i):
                    c += 1
                elif give[i].count(j) == give[j].count(i):
                    a = len(give[i]) - len(receive[i])
                    b = len(give[j]) - len(receive[j])
                    if a > b:
                        c += 1

            else:
                a = len(give[i]) - len(receive[i])
                b = len(give[j]) - len(receive[j])
                if a == b:continue

                elif a > b:
                    c += 1

        result[i] = c

    return max(result.values())

