#/usr/bin/env python2
#-*- coding: utf-8 -*-

'''
 @author Korkeat W. <khasathan@gmail.com>
'''

import re
from config import config
from lib.nlp import helper, tokenizer
from BeautifulSoup import BeautifulSoup
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

def clean_tags(text):
    '''
     Remove only html tags (don't remove text in tags).
    '''
    beautisoup = BeautifulSoup(text)
    return beautisoup.getText().strip()

def clean_html(text):
    '''
     Remove unnecessary html elements.
    '''
    text = re.sub(r'(?i)<!doctype.*>', '', text)
    text = re.sub(r'(?i)<head>.*</head>', '', text)
    text = re.sub(r'(?i)<script.*>.*</script>', '', text)
    text = re.sub(r'(?i)<style.*>.*</style>', '', text)
    text = re.sub(r'<!--.*-->', '', text)
    text = clean_tags(text)
    return text.strip()

def _punkt_sent_tokenize(text):
    '''
     Sentence segmentation using nltk PunktSentenceTokenizer.
    '''
    punkt_param = PunktParameters()
    punkt_param.abbrev_types = set(config.tokenize_abbrev)
    sentence_splitter = PunktSentenceTokenizer(punkt_param)
    return sentence_splitter.tokenize(text)

def _custom_sent_tokenize(text):
    '''
     Sentence segmentation using custom algorithm.
    '''
    return tokenizer.sent_tokenize(text)

def sent_tokenize(text):
    '''
     Wrapper function for sentence segmentation.
    '''
    return _custom_sent_tokenize(norm_text(text))

def norm_text(text):
    '''
     Text normalization function.
    '''
    # add one white space after full stop
    text = re.sub(r'([0-9a-zA-Z]+\.)([0-9a-zA-Z]\.)', r'\1 \2', text)
    text = re.sub(r'(\.|\.\,)([\(\[\{0-9a-zA-Z]{2,})', r'\1 \2', text)
    # remove newline, return and optimize whitespace
    text = helper.remove_newline(text)
    text = helper.optimize_space(text)
    return text.strip()
