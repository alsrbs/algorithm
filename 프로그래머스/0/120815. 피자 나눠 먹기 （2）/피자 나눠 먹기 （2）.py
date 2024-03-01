def solution(n):
    answer = 0
    t = 6
    
    while True:
        if t%n == 0:
            answer = t//6
            break
        t += 6
        
    return answer