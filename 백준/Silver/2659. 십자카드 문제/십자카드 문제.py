from itertools import product

# 입력 카드 값과 네 가지 회전 조합으로 시계수 생성
cards = input().split()
rotations = [''.join(cards[i:] + cards[:i]) for i in range(4)]
clock_number = min(int(rotation) for rotation in rotations)

# 가능한 모든 시계수를 생성하고 중복을 제거하여 정렬
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
unique_clock_numbers = sorted(
    {min(int(''.join(p[i:] + p[:i])) for i in range(4)) for p in product(nums, repeat=4)}
)

# 시계수의 순서 찾기
position = unique_clock_numbers.index(clock_number) + 1
print(position)
