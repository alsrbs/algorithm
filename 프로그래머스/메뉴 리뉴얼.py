from itertools import combinations
from collections import Counter

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

answer = []

for i in course:

    menu_list = []
    for j in orders:
        comb = list(combinations(j, i))

        # 모든 종류의 메뉴
        for menu in comb:
            menu_list.append(''.join(sorted(menu)))
    sorted_menu = sorted(Counter(menu_list).items(), key=lambda x: x[1], reverse=True) # 많은 순으로 정렬
    print(sorted_menu)
    for menu, c in sorted_menu:
        if c > 1 and c == sorted_menu[0][1]: # 가장 많이 함께 주문된 메뉴
            answer.append(menu)
        else:
            continue

print(sorted(answer))

