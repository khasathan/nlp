#/usr/bin/env python2
#-*- coding: utf-8 -*-

'''
 @author Korkeat W. <khasathan@gmail.com>
 @description word and sentence tokenizer
'''

import re
from lib.nlp import helper

OFFSET_OF_NEXT_WORD = 2
BRACKET_MAP_OPEN = {'[': ']', '(': ')', '{': '}'}
BRACKET_MAP_CLOSE = {']': '[', ')': '(', '}': '{'}
TAILING_CHARS = [':', ';', '?', '!', ',']

def sent_tokenize(text):
    '''
     Sentence segmentation with user specific algorithm.
     NOTE: It's might be better for bioinformatics publication only.
    '''
    text = helper.remove_newline(text)
    text = helper.optimize_space(text)
    sent_list = []
    sent_buf = []
    word_buf = []
    bracket_stack = []
    in_bracket = False
    text_len = len(text)
    max_index = text_len - 1

    for i in range(text_len):
        cur_char = text[i]
        if i == max_index:
            sent_buf.append(''.join(word_buf) + cur_char)
            sent_list.append(helper.optimize_space(' '.join(sent_buf)))
            word_buf = []
            sent_buf = []
            break

        if cur_char == ' ':
            sent_buf.append(''.join(word_buf))
            word_buf = []
        elif cur_char in TAILING_CHARS:
            word_buf.append(cur_char)
            sent_buf.append(''.join(word_buf))
            word_buf = []
        elif cur_char == '.':
            word = ''.join(word_buf)
            if (
                    i + OFFSET_OF_NEXT_WORD < max_index and
                    re.match(r'[A-Z]', text[i + OFFSET_OF_NEXT_WORD]) and
                    not in_bracket and
                    re.match(r'[a-z\)\]\}]', text[i - 1])
                ):
                sent_buf.append(word + cur_char)
                sent_list.append(helper.optimize_space(' '.join(sent_buf)))
                sent_buf = []
                word_buf = []
            elif re.match(r'[A-Z]', word):
                word_buf.append(cur_char)
            else:
                sent_buf.append(word + cur_char)
                word_buf = []
        elif cur_char in BRACKET_MAP_OPEN:
            word_buf.append(cur_char)
            bracket_stack.append(cur_char)
            in_bracket = True
        elif cur_char in BRACKET_MAP_CLOSE:
            try:
                open_bracket = bracket_stack.pop()
                if BRACKET_MAP_CLOSE[cur_char] == open_bracket:
                    word_buf.append(cur_char)
                else:
                    word_buf.append(BRACKET_MAP_OPEN[open_bracket])
            except IndexError:
                word_buf.append('')
            in_bracket = False
        else:
            word_buf.append(cur_char)

    return sent_list

def word_tokenize(text, clean=False):
    '''
     Tokenize sentence to words. In this version, we split by special characters.
     If optional parameter 'clean' is set, special characters will cleaned.
    '''
    tokens = _clean_space(re.split(r'([\W\.]+)', text))
    if clean:
        tokens = _clean_special_chars(tokens)
    return tokens

def _clean_space(tokens):
    return filter(lambda token: token != ' ', tokens)

def _clean_special_chars(tokens):
    return filter(lambda token: re.match(r'(\w+)', token), tokens)
