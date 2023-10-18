#IMPORTS    
import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd
import numpy as np






def basic_clean(string):
    string = string.lower()
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    string = re.sub(r"[^a-z0-9'\s]", '', string)

    return string


def tokenizer(string):
    tokenize = nltk.tokenize.ToktokTokenizer()
    string = tokenize.tokenize(string)
    return string


def stem(string):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in string]
    
    
    return stems


def lemmatize(string):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in string]
  
    
    return lemmas


def remove_stopwords(string):
    stopwords_english = stopwords.words('english')
    string_with_stopwords_removed = [word for word in string if word not in stopwords_english]
    
    
    return string_with_stopwords_removed