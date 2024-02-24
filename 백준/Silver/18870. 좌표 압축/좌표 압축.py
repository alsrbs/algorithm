import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
list_n = sorted(set(nums))
dic = {list_n[i] : i for i in range(len(list_n))}
print(*[dic[i] for i in nums])
