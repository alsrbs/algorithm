n = input()
num = 0
while n:
    num += 1
    num_str = str(num)
    while len(num_str) > 0 and len(n) > 0:
        if num_str[0] == n[0]:
            n = n[1:]
        num_str = num_str[1:]
print(num)
