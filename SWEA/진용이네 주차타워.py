from collections import deque
n, m = map(int, input().split())
parking = [0]*n
R_i = {}
for i in range(n):
    r = int(input())
    R_i[i] = r

W_i = []
for i in range(m):
    w = int(input())
    W_i.append(w)

wait = deque([])
result = 0
while True:
    try:
        i = int(input())

        if i>0:


    except:
        print(R_i, W_i, parking)
        break
