def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

x, y = A1*B2+A2*B1, B1*B2 # x = 분자 y = 분모
z = gcd(x, y)
print(x//z, y//z)