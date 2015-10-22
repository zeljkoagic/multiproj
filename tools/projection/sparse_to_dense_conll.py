# converts conll with sparse matrices to conll with implicitly column-indexed dense matrices

import utils.conll as conll
import sys
import codecs

file_handle = codecs.open(sys.argv[1], encoding="utf8")
counter = 0

while True:
    sentence, graph = conll.get_next_sentence_and_graph(file_handle)
    if not sentence:
        break
    counter += 1
    for token in sentence:
        print(token, end="\t")
        print(" ".join([str(x) for x in graph[token.idx]]))
    print()
