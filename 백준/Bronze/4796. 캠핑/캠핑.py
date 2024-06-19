t = 0
while True:
    t+=1
    l, p, v = map(int, input().split())
    if [0, 0, 0] == [l, p, v]:break
    print(f'Case {t}: {v//p*l + min(v%p, l)}')