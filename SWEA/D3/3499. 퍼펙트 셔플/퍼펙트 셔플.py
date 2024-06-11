for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    card = input().split()
    result = []
    if len(card)%2!=0:card+=[0]
    for i in range(len(card)//2):
        result+=[card[i], card[i+len(card)//2]]
    if not result[-1]:result.pop()
    print(*result)