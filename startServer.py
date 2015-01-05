from __future__ import print_function
import os
import subprocess
import sys

CURRENT_DIR = os.getcwd()
RESOURCE_DIR = "%s/resources" % CURRENT_DIR
WORD_BANK = "%s/words.txt" % RESOURCE_DIR
TMP_WORD_BANK = "%s/words.tmp.txt" % RESOURCE_DIR
PROJECT_DIR = "%s/tinyurl" % CURRENT_DIR

def clean_word_bank():
    lines = open(WORD_BANK, "r").readlines()
    targf = open(TMP_WORD_BANK, "w")
    delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())

    for line in lines:
        scrunched = line.lower().strip().translate(None, delchars)
        print(scrunched, file=targf)

    targf.close()
    os.environ["TMP_WORD_BANK_FILE"] = TMP_WORD_BANK
    
  
def load_word_bank():
    parent_dir = os.getcwd()
    os.chdir(PROJECT_DIR)
    subprocess.call(["python", "manage.py", "wordbank"])
    os.chdir(parent_dir)
  
def manage_app():
    parent_dir = os.getcwd()
    os.chdir(PROJECT_DIR)
    subprocess.call(["python", "manage.py", "migrate"])
    subprocess.call(["python", "manage.py", "runserver", "0.0.0.0:8000"])
    os.chdir(parent_dir)
    

if "--reload" in sys.argv or "-r" in sys.argv:
    clean_word_bank()
    load_word_bank()
    
manage_app()
