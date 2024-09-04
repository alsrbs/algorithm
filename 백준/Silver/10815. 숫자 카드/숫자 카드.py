n = int(input())  # 상근이가 가진 카드의 수
sang_geun_card = list(map(int, input().split()))  # 상근이가 가진 카드의 숫자들
m = int(input())  # 확인할 카드의 수
cards = list(map(int, input().split()))  # 확인할 카드의 숫자들

# 딕셔너리를 이용해 상근이가 가진 카드를 키로 설정하고, 값은 True로 설정
sang_geun_card_dict = {card: True for card in sang_geun_card}

# 각 카드를 확인하고, 상근이가 가지고 있는지 여부를 출력
for card in cards:
    if card in sang_geun_card_dict:
        print(1, end=' ')
    else:
        print(0, end=' ')
