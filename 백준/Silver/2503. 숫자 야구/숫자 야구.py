from itertools import permutations

def strike(x, y):
    s = 0
    for i in range(3):
        if x[i] == y[i]:
            s += 1
    return str(s)

def ball(x, y):
    b = 0
    for i in range(3):
        if y[i] == x[i]:continue
        if y[i] in x:
            b += 1
    return str(b)

n = int(input())
conditions = [input() for _ in range(n)]
arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
result = 0
for i in list(permutations(arr, 3)):
    num = ''.join(i)
    cnt = 0
    for i in conditions:
        if i[4] == strike(i[0:4], num) and i[6] == ball(i[0:4], num):
            cnt += 1
    if cnt == n:
        result += 1
print(result)
