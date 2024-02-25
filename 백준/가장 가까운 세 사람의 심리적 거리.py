import sys

input = sys.stdin.readline


def mbti_distance():
    global result

    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp = 0
                if i == j or j == k or i == k:continue

                for x in range(4):
                    if mbti[i][x] != mbti[j][x]: tmp += 1
                    if mbti[j][x] != mbti[k][x]: tmp += 1
                    if mbti[i][x] != mbti[k][x]: tmp += 1
                result = min(tmp, result)
                if result == 0:
                    return 0


for _ in range(int(input())):
    n = int(input())
    mbti = list(input().split())
    result = 9999999

    if n > 32:
        print(0)

    else:
        mbti_distance()
        print(result)


