def solution(code):
    ret = ''
    mode = False
    for idx in range(len(code)):
        if code[idx] == '1':
            mode = not mode
            continue
        if mode == False and idx%2 == 0:
            ret += code[idx]
        if mode and idx%2 == 1:
            ret += code[idx]
    return ret if ret else "EMPTY"