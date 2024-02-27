clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
dic = {}

for i in clothes:
    if i[1] not in dic:
        dic[i[1]] = 0
    dic[i[1]] += 1

result = 1

for k, v in dic.items():
    result *= v+1
print(result-1)
