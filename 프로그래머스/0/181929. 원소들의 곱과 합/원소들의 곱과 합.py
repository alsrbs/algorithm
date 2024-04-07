def solution(num_list):
    s, mul = 0, 1
    for i in num_list:
        s += i
        mul *= i
    
    return 1 if s*s > mul else 0
