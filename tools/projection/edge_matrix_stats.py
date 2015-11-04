import utils.conll as conll
import sys
import codecs
from scipy.stats import entropy
import numpy as np
from collections import defaultdict

def softmax(v):
    e = np.exp(v)
    dist = e / np.sum(e)
    return dist



def minshift(m):
    minval = min(m.flatten())
    if minval < 0:
        edge_distribution_minshifted = m - minval
    else:
        edge_distribution_minshifted = m
    return edge_distribution_minshifted



def findcompetingheads(edge_matrix,threshold=0.90):
    headcounter = 0
    for row in edge_matrix[1:]:
        greedyhead = max(row)
        localthreshold = greedyhead * threshold
        headcounter+=len([x for x in row if x >= localthreshold]) - 1 # we deduct 1 for the actual head
    return headcounter

def competingprobmass(edge_matrix):
    greedyheadmass = 0
    softmaxmatrix = softmax(edge_matrix[1:])
    for row in softmaxmatrix:
        greedyheadmass+=max(row)
    return (sum(softmaxmatrix.flatten()) - greedyheadmass) / (sum(softmaxmatrix.flatten()))

def get_average_matrices_per_size(file_handle):
    D = defaultdict(list)
    while True:
        try:
            sentence, graph = conll.get_next_sentence_and_graph(file_handle) ## hm... yield statement much?
            if not sentence:
                break
            dimensions = graph.shape[0]
            D[dimensions].append(graph)
        except Exception as e:
            pass
    for dimensions in D:
        D[dimensions] = np.array(sum(D[dimensions]))

    return D


def main():

    file_handle = codecs.open(sys.argv[1], encoding="utf8")
    average_graphs= get_average_matrices_per_size(file_handle)
    counter = 0

    file_handle = codecs.open(sys.argv[1], encoding="utf8")
    while True:
        try:
            sentence, graph = conll.get_next_sentence_and_graph(file_handle) ## hm... yield statement much?
            if not sentence:
                break
            counter += 1

            edge_distribution = graph.flatten()
            edge_distribution_softmax = softmax(graph).flatten()
            edge_distribution_minshifted = minshift(graph).flatten()

            metrics = {}
            metrics["kl_div_from_avg"] = entropy(edge_distribution_softmax,softmax(average_graphs[graph.shape[0]].flatten()))
            metrics["sigma"] = np.std(edge_distribution)
            metrics["entropy_minshifted"] = entropy(edge_distribution_minshifted)
            metrics["entropy_softmax"] = entropy(edge_distribution_softmax)

            metrics["competing_heads_raw"] = findcompetingheads(graph)
            metrics["competing_heads_norm"] = findcompetingheads(graph)/graph.shape[0]
            metrics["competing_prob_mass_minshifted"] =  competingprobmass(graph)
            v = []
            for k in sorted(metrics.keys()):
                v.append(str(metrics[k]))
            print(" ".join(v))

        except Exception as e:
            print(str(e)+ " : error in :"+" ".join(["sentence number ",str(counter), "in", sys.argv[1]]), file=sys.stderr)



if __name__ == '__main__':
    main()
