# -*- coding: utf-8 -*-
import re
# sys.path.append('./lib')
from tokenizer import generate_tokenizer, tokenize, sentence_split, sentence_split_nonstd, spaces_re


class Segmenter(object, ):
    '''Class segmenter'''

    def __init__(self, lang):
        self.lang = lang
        self.tokenizer = generate_tokenizer(lang)

    def segment(self, sentence):
        """
        Segments a sentence into tokens
        """

        lines = filter(lambda x: x.strip() != '', sentence.replace('\xef\xbb\xbf', '').splitlines())
        result = []
        for line in lines:
            tokens = sentence_split(tokenize(self.tokenizer, unicode(line)), self.lang)
            result.extend(tokens)

        return result



