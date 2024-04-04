def solution(my_string):
    answer = ''
    for i in my_string:
        n = ord(i)
        if 65 <= n <= 90:
            answer += chr(n + 32)
        else: 
            answer += chr(n - 32)
    return answer