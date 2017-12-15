for file in `ls *.txt`; do
	filename=`basename $file .txt`
	iconv -f iso-8859-15 -t utf-8 $file > $filename.utf8.txt
done