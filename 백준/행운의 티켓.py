def Max(ticket):
    target = (len(ticket) // 2)
    max_num = 0
    while True:
        for i in range(len(ticket) - 1):
            if i > target: break
            for j in range(i, len(ticket), target):
                if j + 2 * target > len(ticket): break
                if sum(ticket[j:j + target]) == sum(ticket[j + target:j + 2 * target]):
                    max_num = max(max_num, len(ticket[j:j + target]))
                    return max_num*2

        target -= 1
        if target < 1: return max_num*2

ticket = list(map(int, list(input())))
print(Max(ticket))



