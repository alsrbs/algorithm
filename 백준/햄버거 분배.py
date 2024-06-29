n, k = map(int, input().split())
Bench = list(input())
ans = 0

for i in range(n):
    if Bench[i] == 'P':
        for j in range(max(0, i-k), min(n, i+k+1)):
            if Bench[j]=='H':
                Bench[j]=0
                ans+=1
                break

print(ans)