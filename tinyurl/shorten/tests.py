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

def gen_url_factory(url):
    w = generate_alias(url)
    gu = GeneratedURL(url=url, generated_alias=w)
    gu.save()
    return gu

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
        
    def test_word_bank_exhaust(self):
        g1 = gen_url_factory("http://test.com/121212/hello-rice-bowl/")
        g2 = gen_url_factory("http://test.com/121212/hello-ice-bowl/")
        g3 = gen_url_factory("http://test.com/121212/hello-ice-cold/")
        g4 = gen_url_factory("http://test.com/121212/hello-hot-bowl/")
        
        g5 = gen_url_factory("http://test.com/121212/a1b2c3d4e6ghghw/")
        
        word = WordBank.objects.filter(word="hello")[0]
        self.assertEqual(True, hasattr(word, "generatedurl"))
        self.assertEqual(g5.generated_alias.word, "hello")
