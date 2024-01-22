import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
nums = list(permutations(A))

total = 0
for i in nums:
    total_num = 0
    for j in range(N-1):
        total_num += abs(i[j]-i[j+1])
    total = max(total_num, total)
print(total)