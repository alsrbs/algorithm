def solution(arr, n):
    for i in range(len(arr)%2+1, len(arr), 2):
        arr[i] += n
    if len(arr)%2:
        arr[0] += n
    return arr