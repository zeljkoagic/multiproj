HOME=/home/zagic/multiproj
EUROPARL=data/europarl

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/home/johannsen/software/TurboParser/deps/local/lib:"

for scheme in c07 ud; do
        for lang in `cat $HOME/$EUROPARL/lists/langs_${scheme}.txt`; do
		# 1: train basic unpruned
		GLOG_logtostderr=1 /home/johannsen/software/TurboParser/TurboParser --model_type=basic --labeled=0 --prune_basic=0 --train --file_train=$HOME/data/treebanks/${lang}-${scheme}-train.conllu.clean.lex --file_model=$HOME/tools/turboparser/models/$lang.$scheme.basic.prune0.model
		# 2: train basic pruned
		GLOG_logtostderr=1 /home/johannsen/software/TurboParser/TurboParser --model_type=basic --labeled=0 --prune_basic=1 --train --file_train=$HOME/data/treebanks/${lang}-${scheme}-train.conllu.clean.lex --file_model=$HOME/tools/turboparser/models/$lang.$scheme.basic.prune1.model
		# parse europarl
	done
done

