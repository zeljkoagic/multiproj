HOME=/home/zagic/multiproj
EUROPARL=data/europarl

for scheme in c07 ud; do
        for pruning in p0 p1; do
                for target in `cat $HOME/$EUROPARL/lists/langs_${scheme}.txt`; do
                        VARa=`ls $HOME/$EUROPARL/parallel/delex_onehot/${target}-${scheme}-test.conllu.clean.delex.src*${scheme}-delex-${pruning}.parsed.onehot`
			
			# GOES ONLY WITH p1
			#VARb=`ls $HOME/$EUROPARL/parallel/delex_onehot/${target}-${scheme}-test.conllu.clean.tts.delex.src*${scheme}-delex-${pruning}.parsed.onehot`
			echo $VARa
			#echo 
			#echo "python $HOME/tools/projection/merge_target_matrices.py $VARa > $HOME/$EUROPARL/parallel/delex_onehot/$target.$scheme.$pruning.parsed.onehot.votes"
			#echo python $HOME/tools/projection/merge_target_matrices.py $VARb > $HOME/$EUROPARL/parallel/delex_onehot/$target.$scheme.$pruning.tts.parsed.onehot.votes
		done
	done
done

#sv-c07-test.conllu.clean.delex.src-pl-c07-delex-p1.parsed.onehot
#hu-ud-test.conllu.clean.delex.src-sv-ud-delex-p0.parsed.onehot

