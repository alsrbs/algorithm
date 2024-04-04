def solution(my_string):
    answer = ''
    for i in my_string:
        if i in 'aoieu':continue
        answer += i
    return answer