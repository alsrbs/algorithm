# 1 2 3 4 5 6 7

# 3 4 5 6 7 2
# 1

# 5 6 7 2 4
# 1 3

# 7 2 4 6
# 1 3 5

# 4 6 2
# 1 3 5 7

# 2 6
# 1 3 5 7 4

# 6
# 1 3 5 7 4 2

# 1 3 5 7 4 2 6
from collections import deque

N = int(input())
q = deque([i+1 for i in range(N)])
N_list = []

while True:
    if not q:break
    N_list.append(q.popleft())
    if not q:break
    q.append(q.popleft())
print(*N_list)
