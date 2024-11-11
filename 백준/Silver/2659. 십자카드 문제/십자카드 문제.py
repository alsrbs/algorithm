from itertools import product

# 카드 값을 입력받고, 회전을 통해 4가지 경우의 수로 구성
cards = input().split()
rotations = sorted(int(''.join(cards[i:] + cards[:i])) for i in range(4))

# 가능한 모든 시계수를 생성하고 중복을 제거하여 정렬
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
unique_clock_numbers = sorted(
    {min(int(''.join(p[i:] + p[:i])) for i in range(4)) for p in product(nums, repeat=4)}
)

print(unique_clock_numbers.index(rotations[0]) + 1)
