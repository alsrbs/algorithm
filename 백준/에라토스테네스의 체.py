n, k = map(int, input().split())

nums = [0]*(n+1)

for i in range(2, n+1):
    for j in range(i, n+1, i):
        if nums[j] == 0:
            nums[j] = 1
            k-=1
            if not k:
                print(j)
                exit()
                