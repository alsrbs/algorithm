def solution(data, ext, val_ext, sort_by):
    d_sort = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    new_data = [item for item in data if item[d_sort[ext]] < val_ext]
    new_data.sort(key=lambda x:x[d_sort[sort_by]])
    print(new_data)
    return new_data