prices = [1, 2, 3, 2, 3]
answer = []

for i in range(len(prices)):

    c = 0
    for j in range(i+1, len(prices)):
        if prices[i] > prices[j]:
            c += 1
            break

        c += 1

    answer.append(c)

print(answer)
