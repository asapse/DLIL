import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# FOLDERS
UTILS = './utils'

DATA_DIR = os.path.join(BASE_DIR, 'release1/')
LABELS_DIR = os.path.join(DATA_DIR, 'labels/')
TRANS_MAN = os.path.join(BASE_DIR, 'release1/trans-manu')
TRANS_MAN_DEV_TXT = os.path.join(BASE_DIR, 'release1/trans-manu/dev/txt')

# FILES
DEV_LABELS = os.path.join(BASE_DIR, 'release1/labels/dev.2015.lst')


# Perl scripts
TRS2STM = UTILS + 'trs2stm.pl'
