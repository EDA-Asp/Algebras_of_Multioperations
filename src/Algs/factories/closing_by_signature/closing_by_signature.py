from multiprocessing import Pool



def make_s_close(superposition_imap, gen_args, all_num, sheffer_list=(), bound=None):
    if bound is None:
        bound = all_num
        msg = 'Sh'
    else:
        msg = f'Bond_{bound}'

    def closing_s(basis):
        if any(map(lambda x: x in sheffer_list, basis)):
            return set(), 'Sh'
        alg_close_substitution, new_mops_substitution = set(), basis.copy()
        while 1:
            for fs in map(superposition_imap, gen_args(new_mops_substitution,
                                                       alg_close_substitution)):
                for f in fs:
                    if f not in alg_close_substitution and f not in new_mops_substitution:
                        if f in sheffer_list:
                            return set(), 'Sh'
                        new_mops_substitution.add(f)
                        if len(alg_close_substitution) + len(new_mops_substitution) >= bound:
                            return alg_close_substitution.union(new_mops_substitution), msg
            if not new_mops_substitution:
                break
        return alg_close_substitution, 'Full'

    return closing_s


def make_p_close(superposition_imap, gen_args, all_num, sheffer_list=(), chunk_size=10_000, bound=None):
    if bound is None:
        bound = all_num
        msg = 'Sh'
    else:
        msg = f'Bond_{bound}'

    def closing_p(basis):
        alg_close_substitution, new_mops_substitution = set(), basis.copy()
        with Pool() as pool:
            while 1:
                for fs in pool.imap_unordered(superposition_imap, gen_args(new_mops_substitution,
                                                                           alg_close_substitution), chunk_size):
                    for f in fs:
                        if f not in alg_close_substitution and f not in new_mops_substitution:
                            if f in sheffer_list:
                                return set(), 'Sh'
                            new_mops_substitution.add(f)
                            if len(alg_close_substitution) + len(new_mops_substitution) >= bound:
                                return alg_close_substitution.union(new_mops_substitution), msg
                if not new_mops_substitution:
                    break
        return alg_close_substitution, 'Full'

    return closing_p


def get_closing(superposition_imap, gen_args, all_num, sheffer_list=(), chunk_size=10_000, parallel=True,
                bound=None):
    selector = [make_s_close(superposition_imap, gen_args, all_num, sheffer_list, bound),
                make_p_close(superposition_imap, gen_args, all_num, sheffer_list, chunk_size, bound)]

    return selector[parallel]
