x = int(input())
line = 1
while x > line:
    x -= line
    line += 1
if line%2 == 0:
    up =  x
    down = line - x + 1
else:
    up = line - x + 1
    down = x
print(f"{up}/{down}")

# • line 1 = 1/1
#   line 2 = 1/2, 2/1
#   line 3 = 3/1, 2/2, 1/3
#   line 4 = 1/4, 2/3, 3/2, 4/1
# • n -= line을 하면 각 line에서 n이 몇번째에 위치하는지 알 수 있다.
# • line이 짝수일때와 홀수일때 분모 분자의 증감 양상이 다르다.
# • 짝수일때는 분모 -1씩 분자 +1씩, 홀수일때는 분모 +1씩 분자 -1씩 증감한다.
