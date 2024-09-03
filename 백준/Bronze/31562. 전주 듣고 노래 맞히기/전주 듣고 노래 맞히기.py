import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic_song = {}
dic_cnt = {}
for _ in range(n):
    song = input().split()
    sound = ''.join(song[2:5])

    if sound not in dic_cnt:
        dic_cnt[sound] = 1
        dic_song[sound] = song[1]
    elif sound in dic_cnt:
        dic_cnt[sound] += 1
        dic_song[sound] = '?'

for _ in range(m):
    sound = ''.join(input().split())

    if sound not in dic_song:
        print('!')
    elif dic_cnt[sound] >= 2:
        print('?')
    else:
        print(dic_song[sound])
