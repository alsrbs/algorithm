def solution(n):
    answer = []
    for i in range(1, n+1):
        if n%i == 0:
            answer += [i, n//i]
    return sorted(set(answer))