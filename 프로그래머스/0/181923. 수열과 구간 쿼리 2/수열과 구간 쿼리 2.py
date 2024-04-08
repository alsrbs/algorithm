def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        n = 1e9
        for i in arr[s:e+1]:
            if i > k:
                n = min(i, n)
        if n == 1e9:
            answer.append(-1)
        else:
            answer.append(n)
    return answer