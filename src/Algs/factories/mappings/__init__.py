from functools import partial

from Algs.Exceptions import AlgSignature
from Algs.factories.mappings.mappings import *


def get_mapping_f_to_num(t, r):
    if t == 'op':
        return partial(mapping_f_num, base=r)
    if t == 'mop':
        return partial(mapping_f_num, base=2 ** r)


def get_mapping_num_to_f(t, r, n):
    if t.startswith('op'):
        base = r
    elif t.startswith('mop'):
        base = 2 ** r
    else:
        raise AlgSignature(expression='', message="signature not start with 'op' or 'mop'")
    l = r ** n
    return partial(mapping_num_f, base=base, l=l)
