def first_rule(words):
    for i in range(len(words)):
        if words[i][0].lower() not in shortcut_key:
            shortcut_key.add(words[i][0].lower())
            words[i] = '[' + words[i][0] + ']' + words[i][1:]
            return True
    return False


def second_rule(words):
    for i in range(len(words)):
        for j in range(1, len(words[i])):
            if words[i][j].lower() not in shortcut_key:
                shortcut_key.add(words[i][j].lower())
                words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j + 1:]
                return True
    return False


n = int(input())
shortcut_key = set()
for _ in range(n):
    words = input().split()

    res = first_rule(words)
    if not res:
        res = second_rule(words)

    print(' '.join(words))

