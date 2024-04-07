def solution(a, b, c):
    l = len(set([a, b, c]))
    if l == 3:
        return a+b+c
    if l == 2:
        return (a+b+c)*(a*a + b*b + c*c)
    if l == 1:
        return (a+b+c)*(a*a + b*b + c*c)*(a*a*a + b*b*b + c*c*c)