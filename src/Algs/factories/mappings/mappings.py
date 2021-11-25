def mapping_f_num(op, base):
    return int(''.join(str(s) for s in op), base)


def mapping_num_f(num, l, base):
    if num == 0:
        return tuple((0 for _ in range(l)))
    nums = []
    while num:
        num, m = divmod(num, base)
        nums.append(m)
    rez = list(reversed(nums))
    while len(rez) < l:
        rez.insert(0, 0)
    return tuple(rez)
