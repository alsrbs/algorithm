def solution(arr, idx):
    n = arr[idx:]
    if 1 not in n:
        return -1
    return n.index(1) + idx
    