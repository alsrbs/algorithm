def solution(genres, plays):
    dic1 = {i: 0 for i in set(genres)}  # 총합
    dic2 = {i: [] for i in set(genres)}  # 장르별 재생횟수

    for i in range(len(genres)):
        dic1[genres[i]] += plays[i]  # 총합
        dic2[genres[i]] += [(plays[i], i)]  # 재생횟수, 인덱스번호

    lst = []
    for i, _ in sorted(dic1.items(), key=lambda x: x[1], reverse=True):
        d = sorted(dic2[i], key=lambda x: x[0], reverse=True)
        if len(d) == 1:
            lst += [d[0][1]]
        else:
            lst += [d[0][1]] + [d[1][1]]
    return lst