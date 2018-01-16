import os
import sys
import warnings
from pathlib import Path

import pandas as pd

from classifiers.basic import BasicClf
from classifiers.personal import PersonalClf
from utils.csv_generator import CSVGenerator
from utils import ctmtocsv


def warn(*args, **kwargs):
    # Used to remove warnings to print
    pass
warnings.warn = warn


def csv_exist(trans, file):
    if trans == 'manu':
        path = Path("../release1/trans-" + trans + "/" + file + ".csv")
        if path.exists():
            return pd.read_csv(path, sep='\t', header=None, names=['id', 'content', 'label'], quoting=3,
                               keep_default_na=False)
        else:
            txt_exist(trans, file)
            csvg = CSVGenerator("trans-" + trans + "/" + file)
            csvg.generate()
            return pd.read_csv(path, sep='\t', header=None, names=['id', 'content', 'label'], quoting=3,
                               keep_default_na=False)
    elif trans == 'auto':
        path = Path("../release2/" + file + ".csv")
        if path.exists():
            return pd.read_csv(path, sep='\t', header=None, names=['id', 'content', 'label'], quoting=3,
                               keep_default_na=False)
        else:
            # gen files
            pass


def txt_exist(trans, file):
    file_path = "../release1/trans-" + trans + "/" + file + "/txt/"
    path = Path(file_path)
    if not path.exists() or os.listdir(file_path) == []:
        os.popen("sh utils/trs2txt-utf8.sh trans-" +
                 trans + "/" + file, "r").read()


def main(argv):
    if argv[1] == "manu":
        train_corpus = csv_exist(argv[1], "train")
        dev_corpus = csv_exist(argv[1], "dev")
    if argv[1] == "auto":
        train_corpus = csv_exist(argv[1], "train")
        dev_corpus = csv_exist(argv[1], "dev")

    basic = BasicClf(train_corpus)
    print("Baseline:")
    basic.evaluate(dev_corpus)

    perso = PersonalClf(train_corpus)
    print("Perso:")
    perso.evaluate(dev_corpus)


if __name__ == "__main__":
    main(sys.argv)
