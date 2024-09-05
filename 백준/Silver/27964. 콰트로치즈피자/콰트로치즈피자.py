n = int(input())
toppings = set(input().split())

cnt = 0
for topping in toppings:
    if 'Cheese' == topping[-6:]:
        cnt += 1

if cnt >= 4:
    print('yummy')
else:
    print('sad')
