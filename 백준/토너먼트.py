n, kim, im = map(int, input().split())
cnt = 0
while kim != im:
  kim -= kim//2
  im -= im//2
  cnt += 1
print(cnt)

# 라운드가 올라가 때마다
# 16 8 9
# 8 -> 4 -> 2 -> 1
# 9 -> 5 -> 3 -> 1
