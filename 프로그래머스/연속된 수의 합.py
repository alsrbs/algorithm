num, total = map(int, input().split())
if num%2==0:
    n = (total//num+1) - num//2
else:
    n = (total//num) - num//2
print([n+i for i in range(num)])