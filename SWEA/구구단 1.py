for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    result = 'No'
    for i in range(1, 10):
        if n%i==0 and n//i<=9:
            result='Yes'
            break
    print(result)