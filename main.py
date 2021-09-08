import time

import numpy as np


class SubResult:
    def __init__(self, element_indices, cost):
        self.element_indices = element_indices
        self.cost = cost


def solve(array):
    t1 = time.time()
    n = array.shape[0]

    sub_results = dict()
    for idx, value in enumerate(array[0, :]):
        sub_results[frozenset([idx])] = SubResult([idx], value)

    i = 1
    while i < n:

        new_sub_results = dict()
        for sub_result in sub_results.values():
            indices = np.arange(n)

            new_elems = np.delete(array[i, :], sub_result.element_indices)
            new_indices = np.delete(indices, sub_result.element_indices).tolist()

            for idx, elem in zip(new_indices, new_elems):
                cost = sub_result.cost + elem
                indices = sub_result.element_indices + [idx]
                idx_key = frozenset(indices)

                if idx_key not in new_sub_results or new_sub_results[idx_key].cost > cost:
                    new_sub_results[idx_key] = SubResult(indices, cost)

        sub_results = new_sub_results
        i += 1

    _, min_sub_result = sub_results.popitem()

    print("min sum is {} with indices {}".format(min_sub_result.cost, min_sub_result.element_indices))
    t2 = time.time()

    print("Computation time: {}".format(t2-t1))


if __name__ == '__main__':
    mat = np.loadtxt("matrix20x20.txt")
    solve(mat)
