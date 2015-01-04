__author__ = 'Amar'

import os
from django.core.management.base import BaseCommand, CommandError
from shorten.models import WordBank

class Command(BaseCommand):
    args = 'None'
    help = 'Loads the wordbank'

    def handle(self, *args, **options):
        print "loading word bank"
        try:
            tmp_word_file = os.environ["TMP_WORD_BANK_FILE"]
        except Exception as e:
            parentdir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
            tmp_word_file = "%s/resources/words.tmp.txt" % parentdir

        lines = open(tmp_word_file, "r").readlines()
        for line in lines:
            thisword = line.strip()
            try:
                entry = WordBank.objects.get(word=thisword)
            except WordBank.DoesNotExist:
                obj = WordBank(word=thisword)
                obj.save()