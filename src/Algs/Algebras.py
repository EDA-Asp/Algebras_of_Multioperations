from abc import ABC, abstractmethod


class AlgBase(ABC):

    def __init__(self, n, r, basis, metaoperations):
        self.basis = basis
        self.alg = tuple()  # tuple of nums which represent operations/multioperations
        self.r = r
        self.n = n
        # self.t = t
        self.closed = False
        self.closed_state = None
        self.metaoperations = metaoperations

    @staticmethod
    @abstractmethod
    def mapping_f_to_num(f):
        pass

    @staticmethod
    @abstractmethod
    def mapping_num_to_f(num):
        pass

    @abstractmethod
    def closing(self):
        pass

    @abstractmethod
    def _save_alg(self, closure):
        pass

    @abstractmethod
    def __iter__(self):
        pass
