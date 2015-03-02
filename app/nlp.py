import nltk
import re
import bs4.BeautifulSoup as soup
from collections import Counter

from .utils import Alphabet

XML_TAG_REGEX = re.compile(u'<.*?>')
STOPWORDS = set(nltk.corpus.stopwords.words('english'))

def clean_xml(xml_str):
    #return XML_TAG_REGEX.sub('', xml_str)
    return soup(xml_str).get_text(separator=' ')

def bigram_count(raw_text, n=2):
    tokenized = nltk.word_tokenize(clean_xml(raw_text))
    counts = Counter()
    def bigram_generator():
        for i in range(len(tokenized)-(n-1)):
            yield tuple(tokenized[i:(i+n-1)])



