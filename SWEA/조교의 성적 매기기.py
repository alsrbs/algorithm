for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n, k = map(int, input().split())
    credit = {'A+': n/10, 'A0': n/10*2, 'A-': n/10*3, 'B+': n/10*4, 'B0': n/10*5, 'B-': n/10*6, 'C+': n/10*7, 'C0': n/10*8, 'C-': n/10*9, 'D0': n}
    score = []
    for i in range(n):
        a, b, c = map(int, input().split())
        total = a*0.35 + b*0.45 + c*0.2
        score.append(total)
    for key, v in credit.items():
        if sorted(score, reverse=True).index(score[k-1]) <= v-1:
            print(key)
            break