import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

normal_menu = {}
for _ in range(a):
    k, v = input().split()
    normal_menu[k] = int(v)

specia_menu = {}
for _ in range(b):
    k, v = input().split()
    specia_menu[k] = int(v)

service_menu = []
for _ in range(c):
    service_menu.append(input())

total_order = {'normal_menu': 0, 'specia_menu': 0, 'service_menu': 0}

m = int(input())
for _ in range(m):
    order = input().rstrip()
    if order in normal_menu:
        total_order['normal_menu'] += normal_menu[order]
    elif order in specia_menu:
        total_order['specia_menu'] += specia_menu[order]
    else:
        total_order['service_menu'] += 1

ans = 'Okay'
if (total_order['service_menu'] != 0 and total_order['normal_menu'] + total_order['specia_menu'] < 50000) or (total_order['specia_menu'] != 0 and total_order['normal_menu'] < 20000) or total_order['service_menu'] > 1:
    ans = 'No'

print(ans)
