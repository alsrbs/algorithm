def solution(dots):
    w = []
    l = []

    for i in dots:
        w.append(i[0])
        l.append(i[1])

    return abs(max(w)-min(w))*abs(max(l)-min(l))
