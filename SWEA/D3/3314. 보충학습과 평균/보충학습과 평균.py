for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    score = list(map(int, input().split()))
    for i in range(len(score)):
        if score[i]<40:
            score[i]=40
    print(sum(score)//5)