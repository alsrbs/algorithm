import re
def solution(my_string):
    answer = 0
    for i in re.findall(r"[0-9]+", my_string):
        answer += int(i)
    print(answer)
    return answer