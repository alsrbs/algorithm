def solution(babbling):
    answer = 0
    for i in range(len(babbling)):
        replace_bab = babbling[i].replace("aya", '1').replace("ye", '1').replace("woo", '1').replace("ma", '1')
        if replace_bab.isdigit():
            answer += 1
    return answer

