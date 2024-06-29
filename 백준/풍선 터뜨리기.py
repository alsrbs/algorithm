from  collections import deque

n = int(input())
nums = list(map(int, input().split()))
q = deque([(i, v) for i, v in enumerate(nums)])

while q:
    x = q.popleft()
    print(x[0]+1, end=' ')
    if x[1]>0:
        q.rotate(-x[1]+1)
    else:
        q.rotate(-x[1])