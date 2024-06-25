for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    
    n = int(input())
    data = []
    
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if data:
            for ad, bd in data:
                if (ad<a and bd>b) or (ad>a and bd<b):
                    ans += 1
    
        data.append((a, b))
    
    print(ans)