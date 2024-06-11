for _ in range(int(input())):
    t, n = input().split()
    print(t)
    num_word = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_dic = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

    word_list = input().split()
    num_list = []
    for i in word_list:
        num_list.append(num_dic[i])

    for i in sorted(num_list):
        print(num_word[i], end=' ')
    print()