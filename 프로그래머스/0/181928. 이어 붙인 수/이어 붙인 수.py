def solution(num_list):
    n, m = '', ''
    for i in num_list:
        if i%2 == 0:
            m += str(i)
        else:
            n += str(i)
    return int(n) + int(m)