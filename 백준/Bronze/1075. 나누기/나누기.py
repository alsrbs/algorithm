n = int(input())
f = int(input())
num = list(str(n))
num[-1] = '0'
num[-2] = '0'
num = int(''.join(num))

answer = None
for i in range(100):
    if num%f == 0:
        answer = str(num)
        break
    num += 1

print(answer[-2] + answer[-1])