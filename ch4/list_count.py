def list_count(lst):
    if len(lst) == 0:
        return 0
    return 1 + list_count(lst[1:])

print(list_count([1, 2, 3, 4, 5]))
