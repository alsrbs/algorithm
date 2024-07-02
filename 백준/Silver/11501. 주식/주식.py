t = int(input())
for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))

    top = stock[-1]
    ans = 0
    for i in range(n-2, -1, -1):
        if top <= stock[i]:
            top = stock[i]
        else:
            ans += top - stock[i]

    print(ans)