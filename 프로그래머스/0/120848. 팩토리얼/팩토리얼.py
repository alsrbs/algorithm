def solution(n):
    answer = 1
    for i in range(2, 11):
        answer *= i
        if answer == n:
            return i
        if answer > n:
            return i - 1
