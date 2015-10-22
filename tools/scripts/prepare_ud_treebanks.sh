HOME=/home/zagic/multiproj
DATA=$HOME/data

#for dir in `ls $DATA/conll/`; do
	for file in $DATA/conll/$dir/*train.conllu; do
		python prepare_ud_treebank.py $file lex > $file.clean.lex
	done
#done

