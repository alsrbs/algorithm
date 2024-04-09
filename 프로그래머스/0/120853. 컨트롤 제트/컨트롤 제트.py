def solution(s):
    answer = 0
    s = s.split()
    for i in range(len(s)):
        if s[i] == 'Z' or (i < len(s)-1 and s[i+1] == 'Z'):continue
        answer += int(s[i])
        
    return answer