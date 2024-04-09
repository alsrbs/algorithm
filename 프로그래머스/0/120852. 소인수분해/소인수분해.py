def solution(n):
    answer = []
    
    for i in range(2, n):
        if n%i == 0:
            answer.append(i)
            
            while True:
                if n%i != 0:
                    break
                n//=i
                
    return answer if answer else [n]