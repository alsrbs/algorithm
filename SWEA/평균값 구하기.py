t = int(input())
for i in range(t):
    nums = list(map(int, input().split()))
    print(f'#{i+1} {int(round(sum(nums)/len(nums),0))}')