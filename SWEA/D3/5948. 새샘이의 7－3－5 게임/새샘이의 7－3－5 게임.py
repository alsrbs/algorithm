from itertools import permutations

for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    nums = list(map(int, input().split()))
    perm = list(permutations(nums, 3))
    result = sorted(set(sum(i) for i in perm))
    print(result[-5])

