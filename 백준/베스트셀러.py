books = {}
for _ in range(int(input())):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
sorted_dict = dict(sorted(books.items(), key=lambda item: (-item[1], item[0])))
print(list(sorted_dict.keys())[0])