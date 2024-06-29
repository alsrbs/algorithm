for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    
    n = int(input())
    word = input()
    ans = 'No'
    
    if n%2 == 0 and word[:n//2] == word[n//2:]:
        ans = 'Yes'
    
    print(ans)

