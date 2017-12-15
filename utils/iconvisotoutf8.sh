for File in `ls *.txt`; do
	Filename=`basename $File .txt`
	iconv -f iso-8859-15 -t utf-8 $File > $Filename.utf8.txt
done