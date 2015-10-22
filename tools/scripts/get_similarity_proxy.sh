for file in /home/zagic/multiproj/data/europarl/parallel/alignments/*inter; do
	python alignmentstats.py $file > $file.avg_weight
done
