from math import gcd

a = 7
b = 20

b //= gcd(a, b)

while not b%2 or not b%5:
    if b % 2 == 0:
        b//=2
    if b % 5 == 0:
        b//=5

print(b)