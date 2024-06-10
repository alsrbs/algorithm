#  문제 요약
# 1. 표1을 보고 입력받은 문자들을 각각 대응하는 숫자로 변경한다.
# 2. 각 숫자들을 6자리 이진수로 표현하고, 이 이진수들을 한 줄로 쭉 이어 붙인다.
# 3. 한 줄로 쭉 이어붙인 이진수들을 8자리씩 끊어서 십진수로 바꾼다.
# 4. 각각의 십진수를 아스키 코드로 변환한다.

lst = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    password = input()

    bin_word = ''
    for i in password:
        binary_str = bin(lst.index(i))
        bin_word += '0' * (6 - len(binary_str[2:])) + binary_str[2:]

    result = ''
    for i in range(0, len(bin_word), 8):
        result += chr(int(bin_word[i:i+8], 2))
    print(result)