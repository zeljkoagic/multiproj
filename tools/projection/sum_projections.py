import codecs
import sys
from collections import defaultdict, Counter

import numpy as np
import utils.conll as conll

reload(sys)
sys.setdefaultencoding('utf8')

sys.stdin = codecs.getreader('utf8')(sys.stdin)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

projection_files = sys.argv[:-1]  # list of files containing the projections
projection_type = sys.argv[-1]  # unit votes on tree edges vs. matrix voting for subsequent MST-ing

handles = [codecs.open(projection_file, encoding="utf8") for projection_file in projection_files]

current_token_id = 0
votes_for_current_sentence_tokens = []
current_sentence = []

while handles[0].read(1):
    handles[0].seek(-1, 1)

    # get current line from all projections
    current_lines = [handle.readline().strip().split() for handle in handles]
    first_current_line = current_lines[0]

    if first_current_line[0]:
        current_token_id += 1

        if projection_type == "matrix":

            votes_for_current_line = np.zeros(first_current_line[0][10:0])

            for line in current_lines:
                token = line[:10]
                heads = line[10:]
                it = 0
                for h in heads:
                    print it
                    votes_for_current_line[it] += float(h)
                    it += 1

            print conll.ConllToken.from_list(current_lines[0][:8]),
            for item in votes_for_current_line:
                print item,
            print

        elif projection_type == "unit":

            current_sentence.append(conll.ConllToken.from_list(current_lines[0][:8]))

            votes_for_current_token_head = Counter()

            for line in votes_for_current_line:
                votes_for_current_token_head.update(line[6])

            votes_for_current_sentence_tokens[current_token_id] = votes_for_current_token_head

    else:

        if projection_type == "unit":
            for token in current_sentence:
                token.head = votes_for_current_sentence_tokens[token.idx].most_common(0)[0]
                print token

            current_token_id = 0
            votes_for_current_sentence_tokens = []
            current_sentence = []

        print
