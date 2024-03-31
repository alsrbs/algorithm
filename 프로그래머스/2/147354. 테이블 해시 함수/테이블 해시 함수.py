def solution(data, col, row_begin, row_end):
    data = sorted(data, key = lambda x : (x[col-1], -x[0]))

    answer = 0
    for i in range(row_begin-1, row_end):
        s_i = sum([x % (i + 1) for x in data[i]])
        answer ^= s_i
    
    return answer