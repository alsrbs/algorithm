def next_number(n):
    global result

    for idx, j in enumerate(n):
        if num[i - 1] < j:
            num[i - 1], num[idx + i] = num[idx + i], num[i - 1]

            for k in range(len(num)):
                result += str(num[k])
            return


for _ in range(int(input())):
    num = list(map(int, input()))
    result = ''
    res = False

    for i in range(len(num) - 1, -1, -1):
        if result:break
        if num[i] > num[i-1]:
            num[i:] = sorted(num[i:])
            next_number(num[i:])

    if result:
        print(result)
    else:
        print('BIGGEST')

