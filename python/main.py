import sys
import os
from pathlib import Path
import pandas as pd
from csv_generator import CSVGenerator


def csv_exist(trans,file):
	path = Path("../release1/trans-"+trans+"/"+file+".csv")
	if path.exists():
		return pd.read_csv(path, sep='\t', header=None, names=['id', 'content', 'label'], quoting=3, keep_default_na=False)
	else:
		txt_exist(trans,file)
		csvg = CSVGenerator("trans-"+trans+"/"+file)
		csvg.generate()
		return pd.read_csv(path, sep='\t', header=None, names=['id', 'content', 'label'], quoting=3, keep_default_na=False)

def txt_exist(trans,file):
	file_path = "../release1/trans-"+trans+"/"+file+"/txt/"
	path = Path(file_path)
	if not path.exists() or os.listdir(file_path) == []:
		os.popen("sh utils/trs2txt-utf8.sh trans-"+trans+"/"+file, "r").read()


def main(argv):
	if argv[1]=="manu":
		train_corpus = csv_exist(argv[1], "train")
		dev_corpus = csv_exist(argv[1], "dev")

if __name__ == "__main__":
   	 main(sys.argv)