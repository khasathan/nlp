#/usr/bin/env python2
#-*- coding: utf-8 -*-

'''
 @author Korkeat W. <khasathan@gmail.com>
'''

import unittest
from lib.nlp import regexutil

class RegExUtilTest(unittest.TestCase):
    def test_patternsToRegexShouldReturnCorrectRegExObjectWithoutException(self):
        raises = False
        patterns = patterns = ['nov\.', 'sp\.', 'ssp\.']
        text = 'The specie AAA sp. nov.'
        try:
            matcher = regexutil.patterns_to_regex(patterns)
            if matcher.search(text) == None:
                raise Exception('Not match')
        except:
            raises = True
        self.assertFalse(raises)

    def test_combinePatternsShouldReturnRegExString(self):
        expect = '(nov\.|sp\.|ssp\.)'
        patterns = ['nov\.', 'sp\.', 'ssp\.']
        actual = regexutil.combine_patterns(patterns)
        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()
