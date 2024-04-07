def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if i > 0:
            a += d
        if included[i]:
            answer += a
    return answer