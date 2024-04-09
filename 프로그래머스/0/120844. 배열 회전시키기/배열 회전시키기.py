from collections import deque

def solution(numbers, direction):
    q = deque(numbers)
    dic = {"right": 1, "left": -1}
    q.rotate(dic[direction])
    return list(q)