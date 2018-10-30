def quicksort(lst):
    if len(lst) < 2:
        return lst
    p = lst[0]
    left = [i for i in lst[1:] if i < p]
    right = [i for i in lst[1:] if i >= p]
    return quicksort(left) + [p] + quicksort(right)

print(quicksort([1, 5, 2, 5, 3, 9, 6, 4, 7, 0, 1, 8]))
