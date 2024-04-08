def solution(arr):
    stk = []
    for i in arr:
        if not stk or (stk and stk[-1] != i):
            stk.append(i)
        else:
            stk.pop()
    return stk if stk else [-1]