def solution(arr):
    
    if len(arr) < len(arr[0]):
        arr += [[0]*len(arr[0]) for i in range(len(arr[0]) - len(arr))]
        return arr
                       
    x = [0] * (len(arr) - len(arr[0]))
    for i in range(len(arr)):
        arr[i] += x
    return arr