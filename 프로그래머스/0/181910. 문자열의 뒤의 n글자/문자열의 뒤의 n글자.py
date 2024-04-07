def solution(my_string, n):
    answer = ''
    for i in range(len(my_string) - 1, len(my_string) - n - 1, -1):
        answer = my_string[i] + answer
    return answer