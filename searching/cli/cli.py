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
from additionally import color
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import RussianStemmer

# Вывод приглашения к действию в консоли
def init():
    print(f'{color.PURPLE}{color.LOGO}')
    serch_query = input(f'{color.CYAN}{color.LINE}{color.WHITE}')
    return serch_query

# Разбиение запроса на токены
def tokens(query):
    tokenizer = RegexpTokenizer(r'[а-яёa-z0-9]+')
    return tokenizer.tokenize(query.lower())

# Лемматизация (отсечение окончаний)
def lemmatization(token):
    stemmer = RussianStemmer()
    stemmed_tokens = [stemmer.stem(tk) for tk in token]
    return stemmed_tokens

# Упаковка
def pack(query):
    token = tokens(query)
    tokens_with_lemm = lemmatization(token)
    return {'tokens': tokens_with_lemm}
