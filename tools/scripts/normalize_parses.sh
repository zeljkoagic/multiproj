HOME=/home/zagic/multiproj

for file in $HOME/data/europarl/parallel/parsed/*parsed; do
	echo "python $HOME/tools/projection/normalize.py $file > $file.softmaxed"
done

