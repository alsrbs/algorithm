def solution(triangle):
    
    if len(triangle) == 1:
        return triangle[0]
    else:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:  
                    triangle[i][j] += triangle[i - 1][0]  
                elif j == len(triangle[i]) - 1:  
                    triangle[i][j] += triangle[i - 1][-1] 
                else:
                    triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])
        return max(triangle[-1])
