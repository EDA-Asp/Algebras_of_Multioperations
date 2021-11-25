from itertools import product, chain, combinations


def gen_intersection_and_union_binary_new(substitution_new):
    return combinations(substitution_new, 2)


def gen_intersection_and_union_binary_cross_1(substitution_new, substitution_old):
    for x in substitution_new:
        for y in substitution_old:
            yield (x, y)


def binary_intersection_and_union_gen_args(substitution_new, substitution_old):
    it = chain(gen_intersection_and_union_binary_new(substitution_new.copy()),
               gen_intersection_and_union_binary_cross_1(substitution_new.copy(), substitution_old.copy()))
    substitution_old.update(substitution_new)
    substitution_new.clear()
    return it


def gen_substitution_new(substitution_new, rpt):
    return product(substitution_new, repeat=rpt)


def gen_substitution_binary_cross_1(substitution_new, substitution_old):
    for x in substitution_new:
        for y in substitution_old:
            for z in substitution_old:
                yield (x, y, z)
                yield (y, x, z)
                yield (y, z, x)


def gen_substitution_binary_cross_2(substitution_new, substitution_old):
    for x in substitution_new:
        for y in substitution_new:
            for z in substitution_old:
                yield (z, x, y)
                yield (x, z, y)
                yield (x, y, z)


def binary_superposition_gen_args(substitution_new, substitution_old):
    it = chain(gen_substitution_new(substitution_new.copy(), 3),
               gen_substitution_binary_cross_1(substitution_new.copy(), substitution_old.copy()),
               gen_substitution_binary_cross_2(substitution_new.copy(), substitution_old.copy()))

    substitution_old.update(substitution_new)
    substitution_new.clear()
    return it


def gen_substitution_unary_cross_1(substitution_new, substitution_old):
    for x in substitution_new:
        for y in substitution_old:
            yield (x, y)
            yield (y, x)


def unary_superposition_gen_args(substitution_new, substitution_old):
    it = chain(gen_substitution_new(substitution_new.copy(), 2),
               gen_substitution_unary_cross_1(substitution_new.copy(), substitution_old.copy()))

    substitution_old.update(substitution_new)
    substitution_new.clear()
    return it
