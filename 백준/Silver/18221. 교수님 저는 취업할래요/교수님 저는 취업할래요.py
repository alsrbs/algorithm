import sys
input = sys.stdin.readline

n = int(input())
arr = []
pro = None
seong_gyu = None
for i in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums)

    if 5 in nums:
        pro = (i, nums.index(5))
    if 2 in nums:
        seong_gyu = (i, nums.index(2))

x1, x2 = min(pro[0], seong_gyu[0]), max(pro[0], seong_gyu[0])
y1, y2 = min(pro[1], seong_gyu[1]), max(pro[1], seong_gyu[1])

cnt = 0
for x in range(x1, x2+1):
    cnt += arr[x][y1:y2+1].count(1)

if cnt >= 3 and (x1-x2)**2 + (y1-y2)**2 >= 25:
    print(1)
else:
    print(0)