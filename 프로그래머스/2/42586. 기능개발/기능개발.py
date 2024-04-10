def solution(progresses, speeds):
    lst = []
    l = len(progresses)
    a = 0
    while True:
        if a == l:break
        if progresses[a] >= 100:
            c = 0
            while True:
                if a == l or progresses[a] < 100:break
                elif progresses[a] >= 100:
                    c,a=c+1,a+1
            lst.append(c)
        for i in range(l):
            progresses[i] += speeds[i]
    return  lst 