# give folder in parameter (e.g. 'trans-manu/dev')

if [ ! -d ../../release1/$1/txt ]; then
    mkdir ../../release1/$1/txt
fi
for file in `ls ../../release1/$1/*.trs`; do
	filename=`basename $file .trs`
	perl trs2stm.pl $file > $filename.txt
	iconv -f iso-8859-15 -t utf-8 $filename.txt > ../../release1/$1/txt/$filename.utf8.txt
	rm -rf *.txt
done
echo 'Done! Find files in '../../release1/$1/txt/