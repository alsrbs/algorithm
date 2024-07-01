n = int(input())
card = list(map(int, input().split()))

m = int(input())
nums = list(map(int, input().split()))

card_cnt = {}
for i in card:
    card_cnt[i] = card_cnt.get(i, 0) + 1

for i in nums:
  if i in card_cnt:
    print(card_cnt[i], end=' ')
  else:
     print(0, end=' ')