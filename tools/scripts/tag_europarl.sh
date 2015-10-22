HOME=/home/zagic/multiproj
EUROPARL=data/europarl

for scheme in c07 ud; do
	for lang in `cat $HOME/$EUROPARL/lists/langs_${scheme}.txt`; do
		# insert the dummy sentence ends
		awk '{if(NF>0){print}else{print "<sentenceend>"}}' $HOME/$EUROPARL/parallel/t/$lang.t > $HOME/$EUROPARL/parallel/t/$lang.t.temp
		# train treetagger
		# a: create the lexicon
		$HOME/tools/treetagger/cmd/make-lex.perl $HOME/data/treebanks/${lang}-${scheme}-train.conllu.clean.lex.tt > $HOME/tools/treetagger/models/$lang.$scheme.lexicon
		# b: train the model
		$HOME/tools/treetagger/bin/train-tree-tagger $HOME/tools/treetagger/models/$lang.$scheme.lexicon $HOME/data/openclass.$scheme $HOME/data/treebanks/${lang}-${scheme}-train.conllu.clean.lex.tt $HOME/tools/treetagger/models/$lang.$scheme.model -st SENTENCE
		# c: tag the text
		$HOME/tools/treetagger/bin/tree-tagger -token -quiet $HOME/tools/treetagger/models/$lang.$scheme.model $HOME/$EUROPARL/parallel/t/$lang.t.temp > $HOME/$EUROPARL/parallel/tts/$lang.$scheme.tts.temp
		# remove the dummy sentence ends
		awk '{if($1 == "<sentenceend>"){print ""}else{print}}' $HOME/data/europarl/parallel/tts/$lang.$scheme.tts.temp > $HOME/$EUROPARL/parallel/tts/$lang.$scheme.tts
		# convert to conllu
		python $HOME/tools/scripts/tt2conll.py $HOME/$EUROPARL/parallel/tts/$lang.$scheme.tts > $HOME/$EUROPARL/parallel/conllu/$lang.$scheme.tts.conllu.lex
		# validate the model on the test set
		# a: test
		$HOME/tools/treetagger/bin/tree-tagger -token -quiet $HOME/tools/treetagger/models/$lang.$scheme.model $HOME/data/treebanks/${lang}-${scheme}-test.conllu.clean.lex.t > $HOME/tools/treetagger/outputs/${lang}-${scheme}-test.conllu.clean.lex.tts.temp
		# b: convert tagged to conll
		awk '{if($2=="SENTENCE"){print ""}else{print}}' $HOME/tools/treetagger/outputs/${lang}-${scheme}-test.conllu.clean.lex.tts.temp > $HOME/data/treebanks/${lang}-${scheme}-test.conllu.clean.lex.tts
		python $HOME/tools/scripts/tt2conll.py $HOME/data/treebanks/${lang}-${scheme}-test.conllu.clean.lex.tts > $HOME/data/treebanks/${lang}-${scheme}-test.conllu.clean.tts.lex
		# c: evaluate
                /home/zagic/bible/tools/tnt/tnt-diff $HOME/tools/treetagger/outputs/${lang}-${scheme}-test.conllu.clean.lex.tts.temp $HOME/data/treebanks/${lang}-${scheme}-test.conllu.clean.lex.tt > $HOME/tools/treetagger/outputs/$lang.$scheme.eval
	done
done

# remove all the junk
rm $HOME/$EUROPARL/parallel/t/*.temp
rm $HOME/$EUROPARL/parallel/tts/*.temp
rm $HOME/tools/treetagger/outputs/*.temp
