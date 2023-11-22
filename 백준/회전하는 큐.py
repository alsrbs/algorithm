from collections import deque
N, M = map(int, input().split())
list_num = deque([i for i in range(1, N+1)])
nums = list(map(int, input().split()))

cnt = 0
for num in nums:

    if list_num.index(num) > len(list_num)//2:
        idx = list_num.index(num)
        list_num.rotate(abs(idx - len(list_num)))
        cnt += abs(idx - len(list_num))
        list_num.popleft()

    else:
        idx = list_num.index(num)
        list_num.rotate(-idx)
        cnt += idx
        list_num.popleft()

print(cnt)