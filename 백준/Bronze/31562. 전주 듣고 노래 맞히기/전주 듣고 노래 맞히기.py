import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}
for _ in range(n):
    song = input().split()
    dic[song[1]] = ''.join(song[2:5])

for _ in range(m):
    sound = ''.join(input().split())

    title = ''
    cnt = 0
    for k, v in dic.items():
        if cnt >= 2:
            break
            
        if sound == v:
            cnt += 1
            title = k

    if cnt >= 2:
        print('?')
    elif cnt == 1:
        print(title)
    else:
        print('!')
