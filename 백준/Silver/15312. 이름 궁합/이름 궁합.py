first_name = input()
second_name = input()

# 예: A=3, B=2, C=1, ..., Z=1
alphabet_values = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

# 두 이름의 각 문자를 숫자로 변환하여 결합한 리스트 만들기
name_values = []
for i in range(len(first_name)):
    name_values += [alphabet_values[ord(first_name[i]) - ord('A')],
                    alphabet_values[ord(second_name[i]) - ord('A')]]


# 리스트의 길이가 2가 될 때까지 합산하여 계산
while len(name_values) > 2:
    next_values = []
    # 인접한 값들의 합을 구하고 10으로 나눈 나머지를 저장
    for i in range(len(name_values) - 1):
        next_values.append((name_values[i] + name_values[i + 1]) % 10)
    name_values = next_values[:]  # name_values를 업데이트

print(str(name_values[0]) + str(name_values[1]))
