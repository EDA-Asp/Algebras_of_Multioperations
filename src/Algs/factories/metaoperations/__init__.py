from Algs.Exceptions import AlgSignature
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