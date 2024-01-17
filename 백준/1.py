while True:
    try:
        n = int(input())
    except:
        break
    cnt = '1'
    while True:
        if int(cnt) % n == 0:break
        cnt = str(cnt) + '1'
    print(len(str(cnt)))