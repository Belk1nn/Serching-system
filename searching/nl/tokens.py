"""
*********************************************************************
*                                                                   *
*                     Welcome to Soorel                             *
*                                                                   *
*   _________  ____  ____  ________                                 *
*  / ___/ __ \/ __ \/ __ \/ ____/ /                                 *
*  \__ \ / / / / / / /_/ / __/ / /                                  *
* ___/ / /_/ / /_/ / _, _/ /___/ /___                               *
* /____/\____/\____/_/ |_/_____/_____/                              *
*                                                                   *
*                                                                   *
*  Soorel is your go-to Python-based search engine.                 *
*  We aim to provide accurate and relevant search results.          *
*  Happy Searching!                                                 *
*                                                                   *
*********************************************************************
"""

from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import RussianStemmer
import json
import copy

def tokenize(doc, folder):
    tokenizer = RegexpTokenizer(r'[а-яёa-z0-9]+')
    res = copy.deepcopy(doc)
    tokens  = tokenizer.tokenize(res['res'])
    res['tokens'] = list(filter(lambda x: len(x) < 15 and len(x) > 2, tokens))
    with open(folder, 'w') as f:
        f.write(json.dumps(res))
        f.close()

def stem(doc, folder):
    stemmer = RussianStemmer()
    res = copy.deepcopy(doc)
    res['stemmed'] = [stemmer.stem(token) for token in res['tokens']]
    with open(folder, 'w') as f:
        f.write(json.dumps(res))
        f.close()


