for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    nums = [0, 0, 0, 0, 0]
    
    while n!=1:
        if n%2==0:
            nums[0]+=1
            n//=2
        if n%3==0:
            nums[1]+=1
            n//=3
        if n%5==0:
            nums[2]+=1
            n//=5
        if n%7==0:
            nums[3]+=1
            n//=7
        if n%11==0:
            nums[4]+=1
            n//=11
    
    print(*nums)