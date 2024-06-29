n = int(input())
ans = 0

while n:
    s = str(n)
    ans += s.count('1')
    n = int('0' + s.replace('1', ''))

    if n:
        n -= 1
        ans += 1

print(ans)