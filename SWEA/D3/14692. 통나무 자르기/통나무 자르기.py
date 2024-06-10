for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    print('Alice' if int(input())%2==0 else 'Bob')