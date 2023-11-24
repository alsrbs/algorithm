def sreach():
    for i in range(1, len(word)-1):
        word_list = []
        for j in range(len(word)):
            if j+i < len(word):
                if word[j]+word[i+j] in word_list:
                    return ' is NOT surprising.'
                else:
                    word_list += [word[j]+word[i+j]]
    return ' is surprising.'

while True:
    word = input()
    if word == '*':
        break
    print(word + sreach())