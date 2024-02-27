def solution(clothes):
    
    dic = {}
    
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]] = 0
        dic[i[1]] += 1
        
    result = 1
    for k, v in dic.items():
        result *= v+1
        
    return result-1