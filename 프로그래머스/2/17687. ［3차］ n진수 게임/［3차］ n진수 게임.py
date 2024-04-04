def solution(n, t, m, p):
    notation = "0123456789ABCDEF"
    result = '0'

    for i in range(1, m*t):
        num = ''
        while i > 0:
            i, remainder = divmod(i, n)
            num += notation[remainder]
        result += num[::-1]
        
    return result[p-1::m][:t]