for i in range(int(input())):
    h, w, n = map(int, input().split())
    yy = n%h
    xx = n//h+1
    if yy == 0:
        xx -= 1
        yy = h
    print(yy*100+xx)