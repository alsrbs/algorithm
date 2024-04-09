def solution(my_string, m, c):
    answer = ''
    if m == 1:
        return my_string
    for i in range(len(my_string)):
        if c-1 == i%m:
            answer += my_string[i]
    return answer