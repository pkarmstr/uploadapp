import nltk
import re
from bs4 import BeautifulSoup as soup
from collections import Counter

XML_TAG_REGEX = re.compile(u'<.*?>')
STOPWORDS = set(nltk.corpus.stopwords.words('english'))

def _clean_xml(xml_str):
    #return XML_TAG_REGEX.sub('', xml_str)
    return soup(xml_str).get_text(separator=' ')

def _is_content_word(token):
    return token not in STOPWORDS or (re.match(r'\W+', token) and len(token) < 2)

def ngram_count(fh, n=2):
    total_counts = Counter()
    for line in fh:
        tokenized = nltk.word_tokenize(_clean_xml(line))
        def n_generator():
            for i in range(len(tokenized)-(n)):
                if all(map(_is_content_word, tokenized[i:(i+n)])):
                    yield tuple(tokenized[i:(i+n)])
        total_counts.update(Counter(n_generator()))
    return total_counts

def run(fh):
    counts = ngram_count(fh)
    return counts.most_common(5000)
