def solution(array, n):
    array.sort()
    answer = [999, 0]
    for i in array:
        x = abs(i - n)
        if x == 0:
            return i
        if answer[0] > x:
            answer[0] = x
            answer[1] = i
    return answer[1]