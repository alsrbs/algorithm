def solution(s, skip, index):
    lst = [ord(i) for i in list(skip)]

    st = ''
    for i in list(s):
        
        x = ord(i)
        for j in range(1, index + 1):
            x += 1
            if x > 122:
                x -= 26
            if x in lst:
                while True:
                    if x not in lst:break
                    x += 1
                    if x > 122:
                        x -= 26

        st += chr(x)

    return st