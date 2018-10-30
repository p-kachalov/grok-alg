def list_max(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]

    cur = lst[0]
    rst = list_max(lst[1:])

    return cur if cur > rst else rst
