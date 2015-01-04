from __future__ import print_function
import os

CURRENT_DIR = os.getcwd()
RESOURCE_DIR = "%s/resources" % CURRENT_DIR
WORD_BANK = "%s/words.txt" % RESOURCE_DIR
TMP_WORD_BANK = "%s/words.tmp.txt" % RESOURCE_DIR

def clean_word_bank():
    lines = open(WORD_BANK, "r").readlines()
    targf = open(TMP_WORD_BANK, "w")
    delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())

    for line in lines:
        scrunched = line.lower().strip().translate(None, delchars)
        print(scrunched, file=targf)

    targf.close()
    os.environ["TMP_WORD_BANK_FILE"] = TMP_WORD_BANK


clean_word_bank()
