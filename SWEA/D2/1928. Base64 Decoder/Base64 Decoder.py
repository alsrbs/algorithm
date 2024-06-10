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