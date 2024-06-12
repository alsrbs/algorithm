for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    s = sorted([int(input()) for i in range(n)], reverse=True)
    ave = sum(s)//n
    result = 0
    for i in s:
        if ave>i:break
        result += i-ave
    print(result)