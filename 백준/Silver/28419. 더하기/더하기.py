n = int(input())
arr = list(map(int, input().split()))

odd = 0
even = 0
for i in range(n):
    if i%2 == 0:
        even += arr[i]
    else:
        odd += arr[i]

if n == 3 and odd == even - 2:
    print(-1)
else:
    print(abs(odd-even))