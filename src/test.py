from Algs import alg_factory


if __name__ == '__main__':
    #
    # b_op_1_t_f = (1, 1, 2, 1, 1, 2, 1, 1, 2)
    #
    # b_op_2_t_f = (0, 2, 1, 0, 2, 1, 0, 2, 1)

    # cls_alg = alg_factory("op", 3, 2)
    #
    # basis = {(0, 0, 0, 0, 2, 0, 1, 0, 1),
    #          (0, 0, 0, 1, 1, 1, 2, 2, 2),
    #          (0, 1, 2, 0, 1, 2, 0, 1, 2)}

    # basis = {(1, 1, 1, 1, 4, 1, 2, 1, 2),
    #          (1, 1, 1, 2, 2, 2, 4, 4, 4),
    #          (1, 2, 4, 1, 2, 4, 1, 2, 4)}

    b_op_1_t_f = (1, 1, 2, 1, 1, 2, 1, 1, 2)

    b_op_2_t_f = (0, 2, 1, 0, 2, 1, 0, 2, 1)

    cls_alg = alg_factory('op_2_3,*', parallel=True)

    sh = (1, 2, 0, 2, 0, 1, 0, 0, 0)

    basis = {sh,
             (0, 0, 0, 1, 1, 1, 2, 2, 2),
             (0, 1, 2, 0, 1, 2, 0, 1, 2)}

    a_1 = cls_alg(basis)
    print(cls_alg.metaoperations['*'](b_op_1_t_f, b_op_1_t_f, b_op_1_t_f))
    print(a_1.mapping_f_to_num((0, 0, 0, 0, 2, 0, 1, 0, 1)))
    print(a_1.mapping_f_to_num((0, 0, 0, 1, 1, 1, 2, 2, 2)))


    a_1.closing()
    print(a_1.closed)
    print(a_1.closed_state)
    print(len(a_1.alg))

    print("s")
    # a_1.closing()
