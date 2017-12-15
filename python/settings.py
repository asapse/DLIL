import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# FOLDERS
UTILS = './utils'
TRANS_MAN_DEV_TXT = os.path.join(BASE_DIR, 'release1/trans-manu/dev/txt')

print(TRANS_MAN_DEV_TXT)

# Perl scripts
TRS2STM = UTILS + 'trs2stm.pl'
