def solution(n):
    for i in range(1, 1000):
        if i%3 == 0 or '3' in str(i):
            continue
        n -= 1
        if n == 0:
            return i