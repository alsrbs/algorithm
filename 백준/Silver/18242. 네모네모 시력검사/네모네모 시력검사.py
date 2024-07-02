n, m = map(int, input().split())
arr = []
s =None
c= 0
for i in range(n):
    a = list(input())
    arr.append(a)
    if '#' in a and not s:
        s = (i, a.index('#'))
        c = a.count('#')

if c%2 == 0:
    print('UP')
else:
    if arr[s[0]+c//2][s[1]] == '.':
        print('LEFT')
    elif arr[s[0]+c-1][s[1]+c//2] == '.':
        print('DOWN')
    else:
        print('RIGHT')
