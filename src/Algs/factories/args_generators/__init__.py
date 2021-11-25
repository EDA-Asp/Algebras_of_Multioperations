from Algs.factories.args_generators.args_generators import *


def get_gen_superposition(n):
    if n == 2:
        return binary_superposition_gen_args
    if n == 1:
        return unary_superposition_gen_args

    def gen_substitution_binary_cross_n(substitution_new, substitution_old):
        if substitution_old:
            return filter(lambda x:
                          (not all(map(lambda y: y in substitution_new.copy(), x)))
                          and
                          (not all(map(lambda y: y in substitution_old.copy(), x))),
                          product(substitution_new.union(substitution_old), repeat=n + 1))
        else:
            return ()

    def n_gen_args(substitution_new, substitution_old):

        it = chain(gen_substitution_new(substitution_new.copy(), n + 1),
                   gen_substitution_binary_cross_n(substitution_new.copy(), substitution_old.copy()))

        substitution_old.update(substitution_new)
        substitution_new.clear()
        return it

    return n_gen_args


def get_gen_intersection_and_union(n):
    if n == 2:
        return binary_intersection_and_union_gen_args

    def gen_intersection_and_union_new_n(substitution_new):
        return combinations(substitution_new, n)

    def gen_intersection_and_union_cross_1_n(substitution_new, substitution_old):
        if substitution_old:
            return filter(lambda x:
                          (not all(map(lambda y: y in substitution_new.copy(), x)))
                          and
                          (not all(map(lambda y: y in substitution_new.copy(), x))),
                          combinations(substitution_new.union(substitution_old), n))
        else:
            return ()

    def n_ary_intersection_and_union_gen_args(substitution_new, substitution_old):
        it = chain(gen_intersection_and_union_new_n(substitution_new.copy()),
                   gen_intersection_and_union_cross_1_n(substitution_new.copy(), substitution_old.copy()))
        substitution_old.update(substitution_new)
        substitution_new.clear()
        return it

    return n_ary_intersection_and_union_gen_args


def get_all_generators(n):
    return get_gen_intersection_and_union(n), get_gen_superposition(n)