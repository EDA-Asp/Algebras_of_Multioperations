from Algs.Algs_exceptions import AlgSignature, AlgMetaoperation
from Algs.factories.metaoperations.metaoperations import *


def get_metaoperation_for_clc(n, r, t):
    if t == 'mop':
        selector = {'*': get_superposition(t=t, r=r, n=n),
                    '-1': get_invert(n, r),
                    'u': get_union(n),
                    'i': get_intersection(n)}
    elif t == 'op':
        selector = {'*': get_superposition(t=t, r=r, n=n)}
    else:
        raise AlgSignature(expression=f't == {t}', message=f"No such type like {t}")
    return selector

def get_superposition(t, r, n):
    selector = [{'op': unary_superposition_op_r(r),  # unary
                 'mop': unary_superposition_mop_r(r),
                 'mop-1': unary_superposition_mop_r_i_r(r)},
                {'op': binary_superposition_op_r(r),  # binary
                 'mop': binary_superposition_mop_r(r),
                 'mop-1': binary_superposition_mop_r_i_r(r)},
                {'op': n_ary_superposition_op_r(r),  # n-ary now mop-1 for n-ary
                 'mop': n_ary_superposition_mop_n_r(n, r)}
                ]

    return selector[n - 1][t] if n < 3 else selector[2][t]


def get_intersection(n):
    if n == 2:
        return binary_intersection
    else:
        return n_ary_intersection


def get_union(n):
    if n == 2:
        return binary_union
    else:
        return n_ary_union


def get_invert(n, r):
    selector = [unary_invert_r(r),  # unary
                binary_invert_r(r),  # binary
                ]
    if n < 3:
        return selector[n - 1]
    else:
        raise AlgMetaoperation(expression='', message=f'invert not implemented for {n}-ary multioprations')


def metaoperation_i(meataoperations_list, invert, args_f):
    rez = {meataoperation(*args_f) for meataoperation in meataoperations_list}
    for mop in rez.copy():
        invert_mop = invert(mop)
        rez.update(invert_mop)
    return tuple(rez)


def metaoperation(meataoperations_list, args_f):
    rez = {meataoperation(*args_f) for meataoperation in meataoperations_list}
    return tuple(rez)


def get_metaoperations_for_closing_by_signature(signature, metaoperations):
    rez = []
    meataoperations_gen_1_list = []

    if 'i' in signature:
        meataoperations_gen_1_list.append(metaoperations['i'])

    if 'u' in signature:
        meataoperations_gen_1_list.append(metaoperations['u'])

    if meataoperations_gen_1_list:
        if '-1' in signature:
            invert = metaoperations['-1']
            rez.append(partial(metaoperation_i, meataoperations_gen_1_list, invert))
        else:
            rez.append(partial(metaoperation, meataoperations_gen_1_list))
    else:
        rez.append([])

    meataoperations_gen_2_list = []

    if '*' in signature:
        meataoperations_gen_2_list.append(metaoperations['*'])

    if meataoperations_gen_2_list:
        if '-1' in signature:
            invert = metaoperations['-1']
            rez.append((partial(metaoperation_i, meataoperations_gen_2_list, invert)))
        else:
            rez.append(partial(metaoperation, meataoperations_gen_2_list))
    else:
        rez.append([])

    return rez