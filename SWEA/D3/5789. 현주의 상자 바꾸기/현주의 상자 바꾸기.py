for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n, q = map(int, input().split())
    box = [0]*n

    for i in range(q):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            box[j] = i+1
    print(*box)
