./cmd/make-lex.perl ../../data/treebanks/${1}-${2}-train.conllu.clean.lex.tt > models/${1}.${2}.lexicon
./bin/train-tree-tagger models/${1}.${2}.lexicon ../../data/openclass.conll ../../data/treebanks/${1}-${2}-train.conllu.clean.lex.tt models/${1}.${2}.model -st SENTENCE
./bin/tree-tagger -token -quiet models/${1}.${2}.model ../../data/treebanks/${1}-${2}-test.conllu.clean.lex.t > TAGGED
~/bible/tools/tnt/tnt-diff TAGGED ../../data/treebanks/${1}-${2}-test.conllu.clean.lex.tt
rm TAGGED

