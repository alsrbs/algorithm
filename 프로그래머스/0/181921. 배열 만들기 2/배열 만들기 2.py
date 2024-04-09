def solution(l, r):
    answer = []
    for num in range(l, r+1):
        s = str(num)
        if len(s) == s.count('5')+s.count('0'):
            answer.append(num)
    return answer if answer else [-1]