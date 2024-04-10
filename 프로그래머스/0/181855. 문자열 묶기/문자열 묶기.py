def solution(strArr):
    answer = {}
    for i in strArr:
        if len(i) not in answer:
            answer[len(i)] = 0
        answer[len(i)] += 1
    return max(answer.values())