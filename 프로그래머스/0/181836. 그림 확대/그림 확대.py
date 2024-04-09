def solution(picture, k):
    answer = []
    for i in picture:
        st = ''
        for j in i:
            st += j*k
        answer += [st] * k
    return answer