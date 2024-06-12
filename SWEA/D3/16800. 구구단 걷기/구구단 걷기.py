for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    print(min([i-1+n//i-1 for i in range(1,  int(n**0.5)+1) if n%i==0]))