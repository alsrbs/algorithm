def solution(sides):
    answer = 0
    sides.sort()
    for i in range(sides[1] - sides[0] + 1, sides[1] + sides[0]):
        answer += 1
    return answer