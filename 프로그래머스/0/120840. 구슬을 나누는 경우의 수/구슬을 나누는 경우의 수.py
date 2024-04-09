def solution(balls, share):
    x = 1
    for i in range(share+1, balls+1):
        x *= i
    
    x1 = 1
    for i in range(1, balls - share + 1):
        x1 *= i
    
    
    return x//x1