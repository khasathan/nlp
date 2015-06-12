#/usr/bin/env python2
#-*- coding: utf-8 -*-

'''
 @author Korkeat W. <khasathan@gmail.com>
 @description helper functions
'''

import re

def optimize_space(text):
    '''
     Remove several whitespace into one, remove whitespace after full stop
     if it located in bracket.
    '''
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(\.) ([\)\]\}])', r'\1\2', text)
    return text.strip()

def remove_newline(text):
    '''
     Remove newline and return (enter) characters.
    '''
    return re.sub(r'[\r\n]+', '', text).strip()
