def solution(num_list):
    answer = 1
    l = len(num_list)
    if l > 10:
        return sum(num_list)
    for i in num_list:
        answer *= i
    return answer