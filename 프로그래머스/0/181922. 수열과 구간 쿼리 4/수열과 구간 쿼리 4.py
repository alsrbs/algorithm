def solution(arr, queries):
    for query in queries:
        s, e, k = query
        for i in range(len(arr)):
            if s <= i <= e and i%k == 0:
                arr[i] += 1
    return arr