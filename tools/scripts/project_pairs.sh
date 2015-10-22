HOME=/home/zagic/multiproj
EUROPARL=data/europarl

for scheme in c07 ud; do
	for pruning in p0 p1; do
		for source in `cat $HOME/$EUROPARL/lists/langs_${scheme}.txt`; do
			for target in `cat $HOME/$EUROPARL/lists/langs_${scheme}.txt`; do
				if [ "$source" != "$target" ]; then
					echo "python $HOME/tools/projection/project.py --source $HOME/$EUROPARL/parallel/parsed/$source.$scheme.tts.conllu.lex.src-${source}-${scheme}-lex-${pruning}.parsed.softmaxed --target $HOME/$EUROPARL/parallel/conllu/$target.$scheme.tts.conllu.lex --aligns $HOME/$EUROPARL/parallel/alignments/${source}-${target}.inter --weight $HOME/$EUROPARL/parallel/alignments/${source}-${target}.inter.avg_weight > $HOME/$EUROPARL/parallel/projections/$target.from_$source.$scheme.$pruning.projection"
				fi
			done
		done
	done
done

