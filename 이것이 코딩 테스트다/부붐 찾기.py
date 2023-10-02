# 1. set으로 있는지 확인
n = int(input())
set_n = set(map(int, input().split()))
m = int(input())
list_m = list(map(int, input().split()))

for i in range(m):
    if list_m[i] in set_n:
        print('yes')
    else:
        print('no')

# 2. 인덱스로 확인
n = int(input())
list_n = list(map(int, input().split()))
m = int(input())
list_m = list(map(int, input().split()))

map_n = [0]*1000000
for i in range(n):
    map_n[list_n[i]] = 1
for i in range(m):
    if map_n[list_m[i]]:
        print('yes')
    else:
        print('no')

# 3. 이진탐색
def search(target, arr, s, e):
    while s <= e:
        m = (s+e)//2
        if arr[m] == target:
            return m
        elif arr[m] > target:
            e = m - 1
        else:
            s = m + 1
        return False

n = int(input())
list_n = sorted(map(int, input().split()))
m = int(input())
list_m = list(map(int, input().split()))

for i in range(m):
    if search(list_m[i], list_n, 0, n):
        print('yes')
    else:
        print('no')