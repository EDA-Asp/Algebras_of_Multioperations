from functools import partial


def superposition_imap_0(pack, fun):
    return fun(*pack)


#
# def function_imap(superposition):
#     def superposition_imap_0(pack):
#         return superposition(*pack)
#     return superposition_imap_0

def function_imap(superposition):
    return partial(superposition_imap_0, fun=superposition)


