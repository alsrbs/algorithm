def solution(myString, pat):
    dic = {'A': 'B', 'B': 'A'}
    st = ''
    for i in myString:
        st += dic[i]
    return 1 if pat in st else 0