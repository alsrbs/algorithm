def solution(arr):
    n = 2
    l = len(arr)
    if l == 1:
        return arr
    while n<l:
        n *= 2
    arr += [0]*(n-l)
    return arr 