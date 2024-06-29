import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}
room_list = []
for i in range(n):
    name = input().strip()
    dic[name] = [0]*18+[1]
    room_list.append(name)

# 사용하는 회의실 표시
for _ in range(m):
    time = input().split()
    for i in range(int(time[1]), int(time[2])):
        dic[time[0]][i] = 1

room_list = sorted(dic.items())

for name, room in room_list:
    room_time = []
    current = 1
    for i in range(9, 19):
        if room[i] == 0 and current == 1:
            s = i
            current = 0
        elif room[i] == 1 and current == 0:
            e = i
            current = 1
            room_time.append((s, e))

    print(f'Room {name}:')
    if room_time:
        print(f'{len(room_time)} available:')

        for time in room_time:
            s = '0'*(2-len(str(time[0]))) + str(time[0])
            e = str(time[1])
            print(f'{s}-{e}')
    else:
        print(f'Not available')

    if room_list[-1][0] != name:
        print('-----')
