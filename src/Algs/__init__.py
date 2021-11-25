from Algs.Algebras import AlgBase
from Algs.Algs_exceptions import AlgIter
from Algs.factories.args_generators import get_all_generators
from Algs.factories.closing_by_signature import get_closing_w
from Algs.factories.mappings import get_mapping_f_to_num, get_mapping_num_to_f
from Algs.factories.metaoperations import get_metaoperation_for_clc, get_metaoperations_for_closing_by_signature
from helpers import parse_signature


def alg_factory(signature, parallel=True, bound=None, sheffer_list=(), chunk_size=10_000):
    t, n, r, metaoperations_s = parse_signature(signature)

    metaoperations = get_metaoperation_for_clc(n, r, t)
    mapping_num_to_f = get_mapping_num_to_f(t, r, r ** n)
    mapping_f_to_num = get_mapping_f_to_num(t, r)
    all_num = r ** (r ** n) if t == 'op' else (2 ** r) ** (r ** n)

    metaoperations_for_closing = get_metaoperations_for_closing_by_signature(metaoperations_s, metaoperations)
    generators_for_closing = get_all_generators(n)

    if '-1' in metaoperations_s:
        closing = get_closing_w(metaoperations_for_closing,
                                generators_for_closing,
                                all_num,
                                bound=bound,
                                sheffer_list=sheffer_list,
                                chunk_size=chunk_size,
                                parallel=parallel, basis_extend=metaoperations['-1'])
    else:
        closing = get_closing_w(metaoperations_for_closing,
                                generators_for_closing,
                                all_num,
                                bound=bound,
                                sheffer_list=sheffer_list,
                                chunk_size=chunk_size,
                                parallel=parallel, basis_extend=None)

    class Alg(AlgBase):

        def __init__(self, basis):
            AlgBase.__init__(self, n, r, basis, metaoperations)

        @staticmethod
        def mapping_f_to_num(f):
            return mapping_f_to_num(f)

        @staticmethod
        def mapping_num_to_f(num):
            return mapping_num_to_f(num)

        def _save_alg(self, closure):
            closure, msg = closure
            if msg == 'Sh':
                self.alg = 'Sh'
                return msg
            else:
                self.alg = tuple((Alg.mapping_f_to_num(f) for f in closure))
                return msg

        @staticmethod
        def make_close(base):
             return closing(base)

        def closing(self):
            self.closed_state = self._save_alg(Alg.make_close(self.basis))
            self.closed = True

        def __iter__(self):
            if self.closed:
                if self.alg != 'Sh':
                    return (Alg.mapping_num_to_f(x) for x in self.alg)
                else:
                    return AlgIter("self.alg != 'Sh'", 'Alg is All fs')
            else:
                raise AlgIter('return (ternary(x, self.r) for x in self.alg)', 'Alg is not closed')

    return Alg