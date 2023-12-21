def reverse_words(segment: str) -> str:
    return ' '.join(word[::-1] for word in segment.split())

def sol(seq: str) -> str:
    seq_list = seq.replace('>', '<').split('<')
    ans = ''

    for i in range(len(seq_list)):
        if i % 2 == 1:
            ans += f'<{seq_list[i]}>'
        else:
            ans += reverse_words(seq_list[i])
    return ans
word = input()
print(sol(word))