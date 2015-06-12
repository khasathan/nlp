#/usr/bin/env python2
#-*- coding: utf-8 -*-

'''
 @author Korkeat W. <khasathan@gmail.com>
'''

import unittest
from lib.nlp import stringutil

class StringUtilTest(unittest.TestCase):
    def setUp(self):
        self.sample_html = '''
        <!doctype html>
        <html>
            <head>
                <!-- comment -->
                <script>var somevar = 0;</script>
            </head>
            <body>
                <h1>Hello World!</h1>
            </body>
        </html>
        '''
        self.sample_paragraph = '''
        Python is a widely used general-purpose, high-level programming
        language. Its design philosophy emphasizes code readability, and its
        syntax allows programmers to express concepts in fewer lines of code
        than would be possible in languages such as C++ or Java. The language
        provides constructs intended to enable clear programs on both a small
        and large scale.
        '''

    def test_stripTagsShouldReturnTextWithoutHtmlTags(self):
        expect = 'doctype htmlcommentvar somevar = 0;Hello World!'
        actual = stringutil.clean_tags(self.sample_html)
        self.assertEqual(expect, actual)

    def test_cleanHtmlShouldReturnTextWithoutContentInHtmlElements(self):
        expect = 'Hello World!'
        actual = stringutil.clean_html(self.sample_html)
        self.assertEqual(expect, actual)

    def test_textShouldReturnListOfSentences(self):
        expect = [
            'Python is a widely used general-purpose, high-level programming language.',
            'Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.',
            'The language provides constructs intended to enable clear programs on both a small and large scale.'
        ]
        norm_text = stringutil.norm_text(self.sample_paragraph)
        actual = stringutil.sent_tokenize(norm_text)
        self.assertEqual(expect, actual)

    def test_normTextShouldStripLeadingTailingWhitespace(self):
        text = '     quick brown fox jumps over lazy dog '
        expect = 'quick brown fox jumps over lazy dog'
        actual = stringutil.norm_text(text)
        self.assertEqual(expect, actual)

    def test_normTextShouldRemoveNewlineAndReturnChar(self):
        text = '''
        quick brown fox
        jumps over lazy dog
        '''
        expect = 'quick brown fox jumps over lazy dog'
        actual = stringutil.norm_text(text)
        self.assertEqual(expect, actual)

    def test_normTextShouldRemoveManyWhitespace(self):
        text = '     quick brown fox      jumps over     lazy dog '
        expect = 'quick brown fox jumps over lazy dog'
        actual = stringutil.norm_text(text)
        self.assertEqual(expect, actual)

    def test_normTextShouldAddOneSpaceAfterFullStopAndComma(self):
        text = 'XXX sp.nov. YYY gen.nov.AAA sp.,BBB gen.nov.i.e.(gen. nov.) (F. Br.)'
        expect = 'XXX sp. nov. YYY gen. nov. AAA sp., BBB gen. nov. i.e. (gen. nov.) (F. Br.)'
        actual = stringutil.norm_text(text)
        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()
