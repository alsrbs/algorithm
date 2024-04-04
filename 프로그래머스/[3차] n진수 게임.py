n = 2
t = 4
m = 2
p = 1

notation = "0123456789ABCDEF"
result = '0'

for i in range(1, m*t):
    num = ''
    while i > 0:
        i, remainder = divmod(i, n)
        num += notation[remainder]
    result += num[::-1]

print(result[p-1::m][:t])

