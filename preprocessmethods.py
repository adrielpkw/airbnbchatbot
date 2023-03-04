# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:39:56 2022

@author: adrie
"""

import nltk
nltk.download("all")#remove after running this file
from nltk.corpus import stopwords

import re

#function to remove punctuation
import string
string.punctuation

def remove_punctuation(text):
    punctuationfree="".join([i for i in text if i not in string.punctuation])
    return punctuationfree
#store punctuation free text

#convert and store the questions and responses without punctuation to lower case
def lower(text):
    lowertext=text.lower()
    return lowertext

#remove stopwords
STOPWORDS = set(stopwords.words('english'))
def remove_stopwords(text):
    """custom function to remove the stopwords"""
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])



#lemmatization with PoS tagging
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
wordnet_map = {"N":wordnet.NOUN, "V":wordnet.VERB, "J":wordnet.ADJ, "R":wordnet.ADV}
def lemmatize_words(text):
    pos_tagged_text = nltk.pos_tag(text.split())
    return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])




#remove URL
def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)


def special_char(text):
    return re.sub(r"[^a-zA-Z0-9 ]", "", text)



import stopwordsiso
from stopwordsiso import stopwords
STOPWORDSCN = stopwords(["zh"])

def remove_CNstopwords(text):
    """custom function to remove the stopwords"""
    return " ".join([word for word in str(text).split() if word not in STOPWORDSCN])


import jieba
def CNtokenizer(text):
    words = jieba.lcut(text)
    return "".join(words)

STOPWORDSBM = stopwords(["ms"])

def remove_BMstopwords(text):
    """custom function to remove the stopwords"""
    return " ".join([word for word in str(text).split() if word not in STOPWORDSBM])

from spacy.lang.id import Indonesian
nlp = Indonesian()
nlp.add_pipe("lemmatizer", config={"mode": "lookup"})
nlp.initialize()

def BMlemmatizer(text):
    return " ".join([token.lemma_.lower() for token in nlp(text) if not token.is_stop and not token.is_punct])




