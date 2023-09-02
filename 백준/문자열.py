from collections import deque

A, B = input().split()
l = len(B)-len(A)
A += '0'*l
num = 99

def check(a,b):
    global num
    c = 0
    for i in range(len(b)):
        if a[i] != '0' and a[i] != b[i]:
            c += 1
    # 작은 값을 저장
    if num > c:
        num = c

check(A, B)
q = deque(A)
# A의 문자열 위치를 바꿔보며 체크
for i in range(l):
    q.rotate()
    check(q, B)

print(num)