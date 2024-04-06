def solution(arr):
    answer = 0
    tmp = arr[:]
    l = len(arr)
    
    while True:
        for i in range(l):
            if tmp[i] > 50 and tmp[i]%2 == 0:
                tmp[i] = tmp[i]//2
            elif tmp[i] < 50 and tmp[i]%2 == 1:
                tmp[i] = tmp[i]*2+1
                
        if tmp == arr:
            return answer
        arr = tmp[:]
        answer += 1
