def solution(n, control):
    return n + control.count('w') + (-1*control.count('s')) + (10*control.count('d')) + (-10*control.count('a'))