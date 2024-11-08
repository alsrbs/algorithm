first_name = input()
second_name = input()

# 알파벳을 숫자로 매핑하는 리스트 (A-Z 순서로 매핑)
alphabet_values = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

# 두 이름의 각 문자를 숫자로 변환하여 결합한 리스트 만들기
name_values = []
for i in range(len(first_name)):
    name_values += [alphabet_values[ord(first_name[i]) - ord('A')],
                    alphabet_values[ord(second_name[i]) - ord('A')]]

# 리스트의 길이가 2가 될 때까지 반복하여 인접한 원소 합산
while len(name_values) > 2:
    name_values = [(name_values[i] + name_values[i + 1]) % 10 for i in range(len(name_values) - 1)]

print(str(name_values[0]) + str(name_values[1]))
