import sys
from itertools import combinations

input = sys.stdin.readline


def mbti_distance():
    global result

    for i in perm:
        tmp = 0
        if sorted(i) in mbti_list:continue
        for x in range(4):
            if i[0][x] != i[1][x]: tmp += 1
            if i[0][x] != i[2][x]: tmp += 1
            if i[1][x] != i[2][x]: tmp += 1

        mbti_list.append(sorted(i))
        result = min(tmp, result)
        if result == 0:
            return 0


for _ in range(int(input())):
    n = int(input())
    mbti = list(input().split())
    result = 9999999
    mbti_list = []
    if n > 32:
        print(0)

    else:
        perm = list(combinations(mbti, 3))
        mbti_distance()
        print(result)
