from itertools import combinations

number = "4177252841"
k = 4

l = len(number)

num_list = list(number)

comb_list = list(combinations(number, l - k))
result_list = list(''.join(map(str, comb)) for comb in comb_list)

print(max(result_list))