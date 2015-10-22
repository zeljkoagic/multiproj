HOME=/home/zagic/multiproj
EUROPARL=data/europarl

#for file in $HOME/$EUROPARL/parallel/votes/*votes; do
	# echo "java -cp $HOME/tools/ChuLiuEdmonds/target/ChuLiuEdmonds-1.0-SNAPSHOT.jar edu.cmu.cs.ark.cle.Test < $file > $file.msted"
for file in $HOME/$EUROPARL/parallel/projections/*projection; do
	echo "java -cp $HOME/tools/ChuLiuEdmonds/target/ChuLiuEdmonds-1.0-SNAPSHOT.jar edu.cmu.cs.ark.cle.Test < $file > $file.msted"
done

