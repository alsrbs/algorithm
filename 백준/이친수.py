from functools import reduce
N = int(input())
print(reduce(lambda acc, _: acc + [acc[-2] + acc[-1]], range(3, N + 1), [0, 1, 1])[N])