def solution(arr, intervals):
    return sum([arr[i[0]:i[1]+1] for i in intervals], [])