def solution(num_list):
    answer = 0
    for i in num_list:
        while i != 1:
            if i%2 == 1:
                i -= 1
            i //= 2
            answer += 1
    return answer