import numpy as np
from scipy.spatial import cKDTree

import types
from timeit import timeit


trees = [(1, 1), (4, 3), (6, 3), (6, 5)]
wells = [(3, 1), (5, 2), (6, 5)]

def setup_data(n, k):
    data = {'d1': trees,
            'd2': wells,
            'mx': k}
    return data

def f_trees(d1, d2, mx):
    t1 = cKDTree(d1)
    t2  = cKDTree(d2)
    import pdb; pdb.set_trace()
    return t1.count_neighbors(t2, mx)

def f_brute(d1, d2, mx):
    dist2 = np.add.outer(np.einsum('ij,ij->i', d1, d1), np.einsum('ij,ij->i', d2, d2)) - 2*np.einsum('ij, kj', d1, d2)
    return np.count_nonzero(dist2 <= mx*mx)



for n in ([10]):
    data = setup_data(n, 4)
    # print("***************DATA: ", data)
    # import pdb; pdb.set_trace()
    ref = np.array(f_trees(**data))
    print(ref)
    print(f'n = {n}')
    for name, func in list(globals().items()):
        if not name.startswith('f_') or not isinstance(func, types.FunctionType):
            continue
        try:
            assert np.allclose(ref, func(**data))
            print("{:16s}{:16.8f} ms".format(name[2:], timeit(
                'f(**data)', globals={'f':func, 'data':data}, number=10)*100))
        except:
            print("{:16s} apparently failed".format(name[2:]))