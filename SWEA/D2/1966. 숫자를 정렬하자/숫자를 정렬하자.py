for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    print(*sorted(map(int, input().split())))