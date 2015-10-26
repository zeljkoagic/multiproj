from __future__ import division

import argparse
import codecs
#import sys

import utils.alignments as align
import utils.conll as conll

#reload(sys)
#sys.setdefaultencoding('utf8')

#sys.stdin = codecs.getreader('utf8')(sys.stdin)
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

parser = argparse.ArgumentParser(description="Projects dependency trees from source to target via word alignments.")

parser.add_argument("--source", metavar="SRC", required=True, help="source conll file")
parser.add_argument("--target", metavar="TRG", required=True, help="target conll file")
parser.add_argument("--aligns", metavar="ALN", required=True, help="word aligments file")
parser.add_argument("--weight", metavar="WGT", required=False, help="language pair similarity file")

args = parser.parse_args()

# get similarity
# similarity = float(codecs.open(args.weight, encoding="utf8").readline().strip())
similarity = 1

# get the source and target conll file handlers
source_file_handle = codecs.open(args.source, encoding="utf8")
target_file_handle = codecs.open(args.target, encoding="utf8")

counter = -1

# iterate over the alignments
for aln_line in codecs.open(args.aligns, encoding="utf8"):

    # get source & target sentence corresponding to the current alignment
    source_sentence, S = conll.get_next_sentence_and_graph(source_file_handle)
    target_sentence = conll.get_next_sentence(target_file_handle)

    counter += 1

    # sample every fifth sentence (1178375 / 5 = 35675 sentences)
    if counter % 5 != 0:
        continue

    m = len(source_sentence)
    n = len(target_sentence)

    alignment_items = aln_line.strip().split()

    if alignment_items:

        # account for the alignment file format
        pairs = alignment_items[::2]
        probabilities = alignment_items[1::2]

        # Add a column to the alignment matrix, which will be all zeros
        A = align.get_alignment_matrix((m + 1, n + 1), pairs, probabilities)
        T = align.project_to_target(S, A)

        # apply the pair similarity factor
        T *= similarity

        for token in target_sentence:
            print(token, end="\t")
            for item in T[token.idx]:
                print(item, end=" ")
            print()
        print()
