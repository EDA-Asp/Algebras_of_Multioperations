from Algs.factories.args_generators import get_all_generators
from Algs.factories.closing_by_signature.closing_by_signature import get_closing


def get_closing_n(superposition_imap_list, n, all_num, sheffer_list=(), chunk_size=10_000,
                  parallel=False,
                  bound=None, basis_extend=None):
    gen_args_list = get_all_generators(n)

    closings_list = []
    for superposition, gen in zip(superposition_imap_list, gen_args_list):
        if superposition:
            closings_list.append(get_closing(superposition, gen, all_num, sheffer_list, chunk_size, parallel, bound))

    def closing(basis):
        if basis_extend:
            for mop in basis.copy():
                basis.update(basis_extend(mop))

        if any(map(lambda x: x in sheffer_list, basis)):
            return set(), 'Sh'

        if len(closings_list) == 1:
            alg_close = closings_list[0](basis)
            return alg_close
        else:
            saved_rez = [set() for i in range(len(closings_list))]
            cnt = len(closings_list)
            while cnt > 0:
                for idx, closing_alg in enumerate(closings_list):
                    if saved_rez[idx] == basis:
                        cnt = cnt - 1
                        continue
                    else:
                        if cnt <= len(closings_list) -1:
                            cnt = cnt + 1
                    alg_close = closing_alg(set.difference(basis, saved_rez[idx]), saved_rez[idx])
                    if alg_close[1] == 'Sh' or alg_close[1] == 'Bond':
                        return alg_close
                    saved_rez[idx] = alg_close[0]
                    basis = alg_close[0]
            return alg_close
    return closing