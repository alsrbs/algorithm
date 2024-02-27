def solution(n):
    k = 1

    while n != 1:
        n /= 2
        if n % 1 != 0:
            k += 1
            n = int(n)

    return k