for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n, k = map(int, input().split())
    score = sorted(map(int, input().split()), reverse=True)
    print(sum(score[:k]))