for i in range(1, int(input())+1):
    nums = list(map(int, input().split()))
    print(f'#{i} {max(nums)}')