def find_heart():
    global h
    for i in range(n):
        for j in range(n):
            if cookie[i][j] == '*':
                h = (i+2, j+1)
                left_arm(i+1, j-1)
                rigth_arm(i+1, j+1)
                waist(i+2, j)
                return


def left_arm(r, c):
    global l_a
    while c>=0 and cookie[r][c]=='*':
        c-=1
        l_a+=1


def rigth_arm(r, c):
    global r_a
    while c<n and cookie[r][c]=='*':
        c+=1
        r_a+=1


def left_foot(r, c):
    global l_f
    while r<n and cookie[r][c]=='*':
        r+=1
        l_f+=1


def rigth_foot(r, c):
    global r_f
    while r<n and cookie[r][c]=='*':
        r += 1
        r_f += 1


def waist(r, c):
    global w
    while cookie[r][c]=='*':
        r+=1
        w+=1

    left_foot(r, c-1)
    rigth_foot(r, c+1)


n = int(input())
cookie = [input() for _ in range(n)]
h = (0, 0)
l_a = 0
r_a = 0
w = 0
l_f = 0
r_f = 0

find_heart()

print(*h)
print(l_a, r_a, w, l_f, r_f)