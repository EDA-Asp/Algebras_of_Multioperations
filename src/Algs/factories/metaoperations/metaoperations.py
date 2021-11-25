from functools import partial, reduce
from itertools import product


def num_to_set(x):
    powers = []
    i = 1
    cnt = 0
    while i <= x:
        if i & x:
            powers.append(cnt)
        cnt += 1
        i <<= 1
    return tuple(powers)


#  Unary


def unary_superposition_op_r_3(ar_1, op):
    return op[ar_1[0]], op[ar_1[1]], op[ar_1[2]]


def unary_substitution_op(r, ar_1, op):
    rez = [x for x in range(r)]
    for x in rez:
        rez[x] = op[ar_1[x]]
    return tuple(rez)


def unary_superposition_op_r(r):
    if r == 3:
        return unary_superposition_op_r_3
    else:
        return partial(unary_substitution_op, r)


def unary_superposition_mop_r_3(ar_1: tuple, mop: tuple):
    """substitution for unary multioperations.
    :param tuple f: multioperation which.
    :param tuple g: multioperation for
    :rtype: tuple
    """
    dic_mop = {
        1: (0,),
        2: (1,),
        3: (0, 1),
        4: (2,),
        5: (0, 2),
        6: (1, 2),
        7: (0, 1, 2)
    }

    a, b, c = 0, 0, 0
    if ar_1[0] != 0:
        for x in dic_mop[ar_1[0]]:
            a = a | mop[x]
    if ar_1[1] != 0:
        for x in dic_mop[ar_1[1]]:
            b = b | mop[x]
    if ar_1[2] != 0:
        for x in dic_mop[ar_1[2]]:
            c = c | mop[x]
    return a, b, c


def unary_substitution_mop(r, dic_mop, ar_1, mop):  # unary operations r 3
    rez = [0 for _ in range(r)]
    for index, num in enumerate(ar_1):
        if num == 0:
            rez[index] = 0
        else:
            for x in dic_mop[num]:
                rez[index] = rez[index] | mop[x]
    return tuple(rez)


def unary_superposition_mop_r(r):
    if r == 3:
        return unary_superposition_mop_r_3
    else:
        dic_mop = {x: num_to_set(x) for x in range(1, 2 ** r)}

    return partial(unary_substitution_mop, r, dic_mop)


def unary_invert_r_3(mop):
    l = list(map(lambda x: format(x, f'03b'), mop))
    ll = [x[::-1] for x in l]
    rez = [int("".join(x[::-1]), 2) for x in zip(*ll)]
    return tuple(rez)


def unary_invert(r, mop):
    l = list(map(lambda x: format(x, f'0{r}b'), mop))
    ll = [x[::-1] for x in l]
    rez = [int("".join(x[::-1]), 2) for x in zip(*ll)]
    return tuple(rez)


def unary_invert_r(r):
    return partial(unary_invert, r)


def unary_superposition_mop_r_i_3(ar1, mop):
    superposition_rez = unary_superposition_mop_r_3(ar1, mop)
    invert_superposition_rez = unary_invert_r_3
    return superposition_rez, invert_superposition_rez


def unary_superposition_mop_r_i(superposition_f, invert_f, ar1, mop):
    superposition_rez = superposition_f(ar1, mop)
    invert_superposition_rez = invert_f(superposition_rez)
    return superposition_rez, invert_superposition_rez


def unary_superposition_mop_r_i_r(r):
    superposition_mop = unary_superposition_mop_r(r)
    invert_mop = unary_invert_r(r)

    return partial(unary_superposition_mop_r_i, superposition_mop, invert_mop)


#  Binary

def binary_intersection(ar_1, ar_2):
    # ar_1, ar_2 = args_f
    return tuple((a1 & a2 for a1, a2 in zip(ar_1, ar_2)))


def binary_union(ar_1, ar_2):
    # ar_1, ar_2 = args_f
    return tuple((a1 | a2 for a1, a2 in zip(ar_1, ar_2)))


def binary_superposition_op_r_3(ar_1, ar_2, bop):
    return bop[ar_2[0] * 3 + ar_1[0]], bop[ar_2[1] * 3 + ar_1[1]], bop[ar_2[2] * 3 + ar_1[2]], \
           bop[ar_2[3] * 3 + ar_1[3]], bop[ar_2[4] * 3 + ar_1[4]], bop[ar_2[5] * 3 + ar_1[5]], \
           bop[ar_2[6] * 3 + ar_1[6]], bop[ar_2[7] * 3 + ar_1[7]], bop[ar_2[8] * 3 + ar_1[8]]


def binary_superposition_op(r, ar_1, ar_2, op):
    return tuple([op[x * r + y] for x, y in zip(ar_1, ar_2)])


def binary_superposition_op_r(r):
    if r == 3:
        return binary_superposition_op_r_3

    return partial(binary_superposition_op, r)


def binary_superposition_mop_r_3(ar_1, ar_2: tuple, mop):
    """substitution for unary multioperations.
    :param ar_1: multioperation which.
    :param tuple ar_2: multioperation which.
    :param tuple mop: multioperation for
    :rtype: tuple
    """
    dic_mop = {
        1: (0,),
        2: (1,),
        3: (0, 1),
        4: (2,),
        5: (0, 2),
        6: (1, 2),
        7: (0, 1, 2)
    }

    a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    if ar_1[0] != 0 and ar_2[0] != 0:
        for x in dic_mop[ar_1[0]]:
            for y in dic_mop[ar_2[0]]:
                a_1 = a_1 | mop[x * 3 + y]
    if ar_1[1] != 0 and ar_2[1] != 0:
        for x in dic_mop[ar_1[1]]:
            for y in dic_mop[ar_2[1]]:
                a_2 = a_2 | mop[x * 3 + y]
    if ar_1[2] != 0 and ar_2[2] != 0:
        for x in dic_mop[ar_1[2]]:
            for y in dic_mop[ar_2[2]]:
                a_3 = a_3 | mop[x * 3 + y]
    if ar_1[3] != 0 and ar_2[3] != 0:
        for x in dic_mop[ar_1[3]]:
            for y in dic_mop[ar_2[3]]:
                a_4 = a_4 | mop[x * 3 + y]
    if ar_1[4] != 0 and ar_2[4] != 0:
        for x in dic_mop[ar_1[4]]:
            for y in dic_mop[ar_2[4]]:
                a_5 = a_5 | mop[x * 3 + y]
    if ar_1[5] != 0 and ar_2[5] != 0:
        for x in dic_mop[ar_1[5]]:
            for y in dic_mop[ar_2[5]]:
                a_6 = a_6 | mop[x * 3 + y]
    if ar_1[6] != 0 and ar_2[6] != 0:
        for x in dic_mop[ar_1[6]]:
            for y in dic_mop[ar_2[6]]:
                a_7 = a_7 | mop[x * 3 + y]
    if ar_1[7] != 0 and ar_2[7] != 0:
        for x in dic_mop[ar_1[7]]:
            for y in dic_mop[ar_2[7]]:
                a_8 = a_8 | mop[x * 3 + y]
    if ar_1[8] != 0 and ar_2[8] != 0:
        for x in dic_mop[ar_1[8]]:
            for y in dic_mop[ar_2[8]]:
                a_9 = a_9 | mop[x * 3 + y]

    return a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9


def binary_superposition_mop(r, dic_mop, ar_1, ar_2, mop):
    """substitution for unary multioperations.
    """
    rez = [0 for _ in range(r ** 2)]
    for i, (x, y) in enumerate(zip(ar_1, ar_2)):
        if x != 0 and y != 0:
            for a in dic_mop[x]:
                for b in dic_mop[y]:
                    rez[i] = rez[i] | mop[a * r + b]
    return tuple(rez)


def binary_superposition_mop_r(r):
    if r == 3:
        return binary_superposition_mop_r_3
    dic_mop = {x: num_to_set(x) for x in range(1, 2 ** r)}
    return partial(binary_superposition_mop, r, dic_mop)


def binary_invert(r, invert, mop):
    # invert by 1 ar
    rez_1 = []
    for unary in (mop[i:i + r] for i in range(0, len(mop), r)):
        rez_1.extend(invert(unary))
    rez_2 = [0 for _ in mop]
    # invert by 2 ar
    for x in range(r):
        temp = tuple((mop[y * r + x] for y in range(r)))
        u_invert = invert(temp)
        for y in range(r):
            rez_2[y * r + x] = u_invert[y]
    return tuple(rez_1), tuple(rez_2)


def binary_invert_r(r):
    invert = unary_invert_r(r)
    return partial(binary_invert, r, invert)


def binary_superposition_mop_r_i(superposition_f, invert_f, ar1, ar2, mop):
    superposition_rez = superposition_f(ar1, ar2, mop)
    invert_1_superposition_rez, invert_2_superposition_rez = invert_f(superposition_rez)
    return superposition_rez, invert_1_superposition_rez, invert_2_superposition_rez


def binary_superposition_mop_r_i_r(r):
    superposition_mop = binary_superposition_mop_r(r)
    invert_mop = binary_invert_r(r)
    return partial(binary_superposition_mop_r_i, superposition_mop, invert_mop)


#  N-ary


def n_ary_intersection(*mops):
    return tuple((reduce(lambda x, y: x & y, a) for a in zip(*mops)))


def n_ary_union(*mops):
    return tuple((reduce(lambda x, y: x | y, a) for a in zip(*mops)))


def superposition_mop(r, n, dic_mop, *mops):
    rez = [0 for _ in range(r ** n)]
    *mops, mop = mops
    for idx, (ss) in enumerate(zip(*mops)):
        if all((x != 0 for x in ss)):
            l = [[i for i in dic_mop[x]] for x in ss]
            for pairs in product(*l):
                rez[idx] = rez[idx] | mop[int(''.join(str(s) for s in pairs), r)]
    return tuple(rez)


def n_ary_superposition_mop_n_r(n, r):
    dic_mop = {x: num_to_set(x) for x in range(1, 2 ** r)}
    return partial(superposition_mop, r, n, dic_mop)


def superposition_op(*ops, r):
    *ops, op = ops
    return tuple([op[int(''.join(str(s) for s in ss), r)] for ss in zip(*ops)])


def n_ary_superposition_op_r(r):
    return partial(superposition_op, r=r)








if __name__ == '__main__':
    # # tmop = a_2 = (2, 2, 4, 1, 0, 0, 1, 2, 4)
    #
    # tmop_2 = (4, 5, 7)
    #
    # e = (1, 2, 4, 1, 2, 4, 1, 2, 4)
    # a_2 = (2, 2, 4, 1, 6, 5, 1, 2, 4)

    # invert = unary_invert_r(3)
    #
    # invert_2 = binary_invert_m1_r(3)
    #
    # rez1 = invert(tmop_2)
    # rez2 = invert(tmop_2)
    #
    # rez4 = invert_2(tmop)
    # rez5 = invert_2(tmop)

    # print(unary_invert((4, 5, 7)))
    # print(binary_invert_r(3)(a_2))

    t_mop_1 = (3, 5, 6, 7, 5, 2, 2, 3, 1)
    t_mop_2 = (5, 3, 2, 5, 6, 3, 2, 0, 7)
    t_mop_3 = (1, 5, 2, 0, 5, 0, 4, 1, 2)

    s_1 = binary_superposition_mop_r(3)
    s_2 = n_ary_superposition_mop_n_r(2, 3)

    print(s_1(t_mop_1,t_mop_2,t_mop_3))
    print(s_2(t_mop_1, t_mop_2, t_mop_3))
    print(s_2(t_mop_1, t_mop_2, t_mop_3))
    print(s_2(t_mop_1, t_mop_2, t_mop_3))
    #
    # print(biary_invert_M2_r_3(tmop))
