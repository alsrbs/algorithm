for t in range(1, 11):
    print(f'#{t}', end=' ')
    n = int(input())
    keyboard = [list(input()) for _ in range(8)]
    keyboard_t = list(zip(*keyboard))
    cnt = 0
    for i in range(8):
        for j in range(8-n+1):
            if ''.join(keyboard[i][j:j+n]) == ''.join(keyboard[i][j:j+n][::-1]):cnt+=1
            if ''.join(keyboard_t[i][j:j+n]) == ''.join(keyboard_t[i][j:j+n][::-1]):cnt+=1
    print(cnt)
