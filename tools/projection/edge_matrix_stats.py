import utils.conll as conll
import sys
import codecs
from scipy.stats import entropy
import numpy as np

def softmax(v):
    e = np.exp(v)
    dist = e / np.sum(e)
    return dist





file_handle = codecs.open(sys.argv[1], encoding="utf8")
counter = 0


def findcompetingheads(edge_matrix,threshold=0.90):
    headcounter = 0
    for row in edge_matrix[1:]:
        greedyhead = max(row)
        localthreshold = greedyhead * threshold
        headcounter+=len([x for x in row if x >= localthreshold]) - 1 # we deduct 1 for the actual head
    return headcounter



while True:
    try:
        sentence, graph = conll.get_next_sentence_and_graph(file_handle) ## hm... yield statement much?
        if not sentence:
            break
        counter += 1

        print(graph.shape)
        edge_distribution = graph.flatten() # it might contain negative numbers
        minval = min(edge_distribution)

        if minval < 0:
            edge_distribution_minshifted = edge_distribution - minval
        else:
            edge_distribution_minshifted = edge_distribution

        metrics = {}
        metrics["entropy_minshifted"] = entropy(edge_distribution_minshifted)
        metrics["entropy_softmax"] = entropy(edge_distribution_minshifted)
        metrics["competing_heads_raw"] = findcompetingheads(graph)
        metrics["competing_heads_norm"] = findcompetingheads(graph)/graph.shape[0]
        metrics["competing_prob_mass"] =  0 # the amount of prob mass left when you greedily remove heads from the roster
        metrics["mutual_information_or_KL_wrt_to_average"] =  0 # the amount of prob mass left when you greedily remove heads from the roster




        v = []
        for k in sorted(metrics.keys()):
            v.append(str(metrics[k]))
        print(" ".join(v))

    except Exception as e:
        print(str(e)+ " : error in :"+" ".join(["sentence number ",str(counter), "in", sys.argv[1]]), file=sys.stderr)

