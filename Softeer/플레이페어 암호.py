def check(a, b):
    global ans

    a_point = None
    b_point = None

    for i in range(5):
        for j in range(5):
            if arr[i][j] == a:
                a_point = (i, j)
            if arr[i][j] == b:
                b_point = (i, j)

        if a_point and b_point:
            break

    # 같은 행
    if a_point[0] == b_point[0]:
        ans += arr[a_point[0]][(a_point[1] + 1) % 5] + arr[b_point[0]][(b_point[1] + 1) % 5]
    # 같은 열
    elif a_point[1] == b_point[1]:
        ans += arr[(a_point[0] + 1) % 5][a_point[1]] + arr[(b_point[0] + 1) % 5][b_point[1]]
    # 3번 케이스
    else:
        ans += arr[a_point[0]][b_point[1]] + arr[b_point[0]][a_point[1]]


s = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
message = input()
word = input()

# 5X5 표 만들기
arr = [[0]*5 for _ in range(5)]
w = ''
for i in word+s:
    if i not in w:
        w+=i
        x_idx = len(w)%5
        y_idx = len(w)//5
        if x_idx == 0:
            x_idx = 5
            y_idx -= 1
        arr[y_idx][x_idx-1] = i

ans = ''

# 메세지를 두 글자씩 나누기
idx = 0
while idx < len(message):
    if idx+1<len(message):
        if message[idx] != message[idx+1]:
            check(message[idx], message[idx+1])
            idx += 2
        else:
            if message[idx]+message[idx+1] == 'XX':
                check(message[idx], 'Q')
            else:
                check(message[idx], 'X')
            idx += 1
    else:
        if idx == len(message)-1:
            check(message[idx], 'X')
        idx += 1

print(ans)