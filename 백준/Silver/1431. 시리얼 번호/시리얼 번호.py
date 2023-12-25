import re

def custom_sort(item):
    numbers = [int(num) for num in re.findall(r'\d', item)]
    return (len(item), sum(numbers), item)

N = int(input())
words = []
for i in range(N):
    words += [input()]

sorted_words = sorted(words, key=custom_sort)

for word in sorted_words:
    print(word)