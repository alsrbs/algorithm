def solution(arr):
    if 2 not in arr:
        return [-1]
    s, e = 0, len(arr)-1
    while True:
        if arr[s] == 2 and arr[e] == 2 or s == e:
            return arr[s:e+1]
        if arr[s] != 2:
            s += 1
        if arr[e] != 2:
            e -= 1