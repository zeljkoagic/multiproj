import codecs
import re
from subprocess import check_call, PIPE
from tempfile import NamedTemporaryFile
import argparse

import pandas as pd
from pathlib import Path
import numpy as np

parser = argparse.ArgumentParser(description="""Merge target Chu-Lui-Edmond matrices from multiple sources""")
parser.add_argument('input_target_matrices', nargs='+', type=Path)
# parser.add_argument('ouput_target_matrix', help="Write merged result here")

args = parser.parse_args()

input_files = [input_file.open() for input_file in args.input_target_matrices]
num_input_files = len(input_files)

while len(input_files):
    # Check that all input files have the same number of lines
    assert len(input_files) == num_input_files

    conll_part = None
    scores = None

    for input_file in list(input_files):
        line = input_file.readline()
        if line == '':
            input_files.remove(input_file)
        elif line == '\n':
            pass
        else:
            conll_part, score_part = line.rsplit("\t", maxsplit=1)
            # The score part includes a leading '_ ', which we get rid of
            score_part = score_part[2:]

            single_source_scores = np.array(list(map(float, score_part.strip().split())))
            if scores is None:
                scores = single_source_scores
            else:
                scores += single_source_scores

    # assert conll_part

    # Re-insert the underscore
    if conll_part:
        print("{}\t_ {}".format(conll_part, " ".join(map(str, scores))))
    else:
        print()

