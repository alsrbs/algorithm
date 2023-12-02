def solution(elements):
    e = elements + elements
    answer = set()
    for i in range(1, len(elements)):
        for j in range(len(elements)):
            answer.add(sum(e[j:j+i]))
    else:
        answer.add(sum(elements))
    return len(answer)