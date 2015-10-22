# softmax normalization by AJ

from __future__ import division, print_function
import sys
import numpy as np
import pandas as pd

for line in open(sys.argv[1]):
    if line != "\n":
        parts = line.strip().split("\t")
        
        kv_pairs = [kv_pair.split(":") for kv_pair in parts[-1].split()]
        score_dict = {int(k): float(v) for k,v in kv_pairs}
        scores = pd.Series(score_dict)

        softmax = scores.apply(np.exp) / scores.apply(np.exp).sum()
        transformed_pairs = ["{}:{}".format(idx, prob) for idx, prob in softmax.iteritems()]

        print("\t".join(parts[:-1]), end='\t')
        print(" ".join(transformed_pairs))
    else:
        print()
