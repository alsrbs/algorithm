def solution(dirs):
    direction = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

    s = (0, 0)
    result = set()

    for i in dirs:
        x = s[0] + direction[i][0]
        y = s[1] + direction[i][1]

        if -5 <= x <= 5 and -5 <= y <= 5:
            route1 = str(s[0]) + str(s[1]) + str(x) + str(y)
            route2 = str(x) + str(y) + str(s[0]) + str(s[1])
            result.add(route1)
            result.add(route2)
            s = (x, y)
        
    return len(result)//2