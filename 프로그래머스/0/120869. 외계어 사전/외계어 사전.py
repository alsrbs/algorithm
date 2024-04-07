def solution(spell, dic):
    for i in dic:
        c = 0
        for j in spell:
            if j in i:
                c += 1
            if c == len(spell):
                return 1
    return 2