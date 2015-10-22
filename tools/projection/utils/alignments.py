from __future__ import division
import numpy as np


def get_alignment_matrix(shape, pairs, probabilities):
    """Creates m x n source-target alignment probability matrix.

    :param shape: matrix shape pair, m = source dimension (row indices), n = target dimension (column indices)
    :param pairs: list of source-target index pairs
    :param probabilities: list of probabilities associated with the pairs
    :return: TODO
    """

    if len(pairs) != len(probabilities):
        raise Exception("Mismatch in sizes of pairs (%s) and probabilities (%s)" % (len(pairs), len(probabilities)))

    matrix = np.zeros(shape)  # change here for non-zero default

    for it in range(len(pairs)):
        source_id, target_id = pairs[it].split("-")
        probability = probabilities[it]
        matrix[int(source_id)+1][int(target_id)+1] = float(probability)

    matrix[0, 0] = 1.0  # source root always aligns to target root

    return matrix


def project_to_target(S, A):
    """Projects source graph to target graph via source-target word alignment.

    :param S: source graph (m x m matrix)
    :param A: word alignment matrix (m x n + 1)
    :return: target graph
    """
    m, n_plus_one = A.shape
    
    T = np.zeros(shape=(n_plus_one, n_plus_one))  # target graph
    T_edge = np.zeros_like(T)

    # for each dependent d in source graph (dependents are rows!)
    for d in range(0, m):
            # and for each head of dependent d (heads are columns!)
            for h in range(m):
                confidence = S[d][h]  # get confidence of h->d
                np.dot(A[d].reshape(-1, 1), A[h].reshape(1, -1), out=T_edge)
                T_edge *= confidence
                T += T_edge
    return T
