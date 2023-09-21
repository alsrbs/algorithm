numberToWord = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}
reverse_d = dict(map(reversed, numberToWord.items()))
m, n = map(int, input().split())

number_list = []
for i in range(m, n+1):
    if i < 10:
        number_list += [numberToWord[i]]
    else:
        st = str(i)
        number_list += [numberToWord[int(st[0])] + '.' + numberToWord[int(st[1])]]

sort_num_list = []
for i in sorted(number_list):
    if len(i) < 6:
        sort_num_list += [reverse_d[i]]
    else:
        st_num = i.split('.')
        st = str(reverse_d[st_num[0]]) + str(reverse_d[st_num[1]])
        sort_num_list += [int(st)]

for i in range(0, len(sort_num_list), 10):
    print(*sort_num_list[i:i + 10])
