#/usr/bin/env python2
#-*- coding: utf-8 -*-

'''
 @author Korkeat W. <khasathan@gmail.com>
'''

import unittest
from lib.nlp import stringutil, tokenizer

class TokenizerTest(unittest.TestCase):
    def test_sentTokenizeShouldReturnListOfSentence(self):
        text = '''
        The species was named as Penicillium koreense sp. nov. as it was \
        isolated from various regions in Korea. The specie did not found before \
        (gen. nov.) (F. Br.). Bidens microcephala W.L. Wagner, J.R. Clark &amp; Lorence sp. nov.
        '''
        expect = [
            stringutil.norm_text('The species was named as Penicillium \
            koreense sp. nov. as it was isolated from various regions in Korea.'),
            'The specie did not found before (gen. nov.) (F. Br.).',
            'Bidens microcephala W.L. Wagner, J.R. Clark &amp; Lorence sp. nov.'
        ]
        sent_list = tokenizer.sent_tokenize(text)
        self.assertEqual(expect, sent_list)

    def test_wordTokenizeShouldReturnListOfCharacterWithoutClean(self):
        text = 'The specie did not found before (gen. nov.) (F. Br.).'
        tokenized = tokenizer.word_tokenize(text)
        expect = ['The', ' ', 'specie', ' ', 'did', ' ', 'not', ' ', 'found',
            ' ', 'before', ' (', 'gen', '. ', 'nov', '.) (', 'F', '. ', 'Br',
            '.).', '']
        self.assertEqual(tokenized, expect)

    def test_wordTokenizeShouldReturnListOfCharacterWithoutClean(self):
        text = 'The specie did not found before (gen. nov.) (F. Br.).'
        tokenized = tokenizer.word_tokenize(text, clean=True)
        expect = ['The', 'specie', 'did', 'not', 'found', 'before', 'gen',
            'nov', 'F', 'Br']
        self.assertEqual(tokenized, expect)

if __name__ == '__main__':
    unittest.main()
