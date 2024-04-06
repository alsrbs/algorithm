from collections import Counter

def solution(array):
    answer = Counter(array).most_common() + [(0, 0)]
    return answer[0][0] if answer[0][1] > answer[1][1] else -1