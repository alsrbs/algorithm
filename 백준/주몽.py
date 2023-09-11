n = int(input())
m = int(input())
lst = sorted(map(int, input().split()))
total = 0;s = 0;e = n-1
while True:
    if s >= e:break
    x = lst[s]+lst[e]
    if x == m:
        total+=1;s+=1;e-=1
    elif x>m:
        e-=1
    else:
        s+=1
print(total)