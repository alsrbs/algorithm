numbers = [1, 2, 3]
k = 3

l = len(numbers)
s = 0
for i in range(k-1):
    s = (s + 2) % l
    print(numbers[s])

print(numbers[s])

