import sys
input = sys.stdin.readline


def deadline_check(y, m, d):
    if today > [y, m, d]:
        return "unsafe"
    return "safe"


def monthCheck(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 30


today = list(map(int, input().split()))
n = int(input())

for _ in range(n):
    deadline = list(map(int, input().split()))
    ans = 'invalid'

    # 가능한 모든 날짜 형식 (년, 월, 일) 조합에 대해 검사
    for idx in [(0, 1, 2), (2, 1, 0), (2, 0, 1)]:
        yy = deadline[idx[0]]
        mm = deadline[idx[1]]
        dd = deadline[idx[2]]

        # 유효한 날짜인지 확인
        if 1 <= mm <= 12 and 1 <= dd <= monthCheck(yy, mm):
            ans = deadline_check(yy, mm, dd)
            if ans == 'unsafe':
                break

    print(ans)
