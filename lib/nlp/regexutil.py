#/usr/bin/env python2
#-*- coding: utf-8 -*-

'''
 @author Korkeat W. <khasathan@gmail.com>
 @description helper functions
'''

import re

def patterns_to_regex(patterns):
    '''
     Build many patterns into one pattern then compile to regex object.
    '''
    return re.compile(r'(' + '|'.join(patterns) + ')')

def combine_patterns(patterns):
    '''
     Combine patterns to regular expression string.
    '''
    return '(' + '|'.join(patterns) + ')'
