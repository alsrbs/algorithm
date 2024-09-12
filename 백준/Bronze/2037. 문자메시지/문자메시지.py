p, w = map(int, input().split())
word = input()

# 문자-값 매핑
char_to_value = {
    'A': p, 'B': p * 2, 'C': p * 3,
    'D': p, 'E': p * 2, 'F': p * 3,
    'G': p, 'H': p * 2, 'I': p * 3,
    'J': p, 'K': p * 2, 'L': p * 3,
    'M': p, 'N': p * 2, 'O': p * 3,
    'P': p, 'Q': p * 2, 'R': p * 3, 'S': p * 4,
    'T': p, 'U': p * 2, 'V': p * 3,
    'W': p, 'X': p * 2, 'Y': p * 3, 'Z': p * 4,
    ' ': p
}

# 문자-그룹 매핑
char_to_group = {
    'A': 2, 'B': 2, 'C': 2,
    'D': 3, 'E': 3, 'F': 3,
    'G': 4, 'H': 4, 'I': 4,
    'J': 5, 'K': 5, 'L': 5,
    'M': 6, 'N': 6, 'O': 6,
    'P': 7, 'Q': 7, 'R': 7, 'S': 7,
    'T': 8, 'U': 8, 'V': 8,
    'W': 9, 'X': 9, 'Y': 9, 'Z': 9
}

answer = 0
for i in range(len(word)):
    answer += char_to_value[word[i]]

    # 이전 문자와 현재 문자가 같은 그룹에 속하는지 확인
    if i > 0 and word[i-1] != ' ' and char_to_group.get(word[i - 1]) == char_to_group.get(word[i]):
        answer += w

print(answer)
