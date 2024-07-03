n = int(input())
arr = sorted(map(int, input().split()))

if n%2==0:
    print(arr[n//2-1])
else:
    print(arr[n//2])