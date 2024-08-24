n, k = map(int, input().split())
div = []

for i in range(1, int(n**(1/2))+1):
    if n%i == 0:
        div += [n//i, i]

div = sorted(set(div))

if len(div) >= k:
    print(div[k-1])
else:
    print(0)