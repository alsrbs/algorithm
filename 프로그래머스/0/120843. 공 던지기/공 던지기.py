def solution(numbers, k):
    l = len(numbers)
    s = 0
    for i in range(k-1):
        s = (s + 2) % l
    return numbers[s]