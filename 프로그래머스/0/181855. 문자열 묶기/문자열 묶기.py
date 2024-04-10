def solution(strArr):
    answer = [0]*100001
    for i in strArr:
        answer[len(i)] += 1
    return max(answer)