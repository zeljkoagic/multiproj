from __future__ import division

import codecs
import sys

import utils.conll as conll

reload(sys)
sys.setdefaultencoding('utf8')

sys.stdin = codecs.getreader('utf8')(sys.stdin)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

file_handle = codecs.open(sys.argv[1], encoding="utf8")

counter = -1

sentence = "x"

while sentence:

    sentence, one_hot = conll.get_next_sentence_and_onehot(file_handle)

    counter += 1

    # sample every fifth sentence (1178375 / 5 = 35675 sentences)
    #if counter % 5 != 0:
    #    continue

    for i in range(len(sentence)):
        print sentence[i], " ".join(map(str, one_hot[i+1]))
    print