def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        if myString[i] == pat[0] and myString[i:i+len(pat)] == pat:
            answer += 1
    return answer