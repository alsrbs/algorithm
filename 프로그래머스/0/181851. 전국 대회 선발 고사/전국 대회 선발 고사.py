def solution(rank, attendance):
    arr = []
    for i in range(len(rank)):
        if attendance[i]:
            arr.append(rank[i])
    arr.sort()
    return 10000*rank.index(arr[0])+100*rank.index(arr[1])+rank.index(arr[2])