# give folder in parameter (e.g. '../../release1/trans-man/dev'

for file in `ls $1/*.trs`; do
	filename=`basename $file .trs`
	perl trs2stm.pl $file > $filename.txt
	iconv -f iso-8859-15 -t utf-8 $filename.txt > $1/txt/$filename.utf8.txt
	rm -rf *.txt
done