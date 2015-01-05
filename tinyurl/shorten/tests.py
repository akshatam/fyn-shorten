from django.test import TestCase
from shorten.models import GeneratedURL, WordBank
from shorten.views import *
import random

# Create your tests here.

def load_test_wordbank():
    words = ["hello", "ice", "hot", "cold"]
    for word in words:
        w = WordBank(word=word)
        w.save()

class WBValidity(TestCase):
    def setUp(self):
        load_test_wordbank()
        
    def test_url_existing_word_shorten(self):
        testurl = "http://test.com/121212/hello-rice-bowl/"
        w = generate_alias(testurl)
        self.assertEqual("hello", w.word)
        
    def test_url_not_exist_word_shorten(self):
        testurl = "http://test.com/121212/good-rice-bowl/"
        w = generate_alias(testurl)
        self.assertIsInstance(w, WordBank)
