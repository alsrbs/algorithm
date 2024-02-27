from itertools import permutations

def solution(k, dungeons):
    dungeons_idx = [i for i in range(len(dungeons))]
    perm = list(permutations(dungeons_idx, len(dungeons)))
    
    result = 0
    for dungeon_list in perm:
        c = 0
        K = k
        for idx in dungeon_list:

            if dungeons[idx][0] <= K:
                K -= dungeons[idx][1]
                c += 1

                if K == 0:
                    break
        result = max(c, result)
    return result