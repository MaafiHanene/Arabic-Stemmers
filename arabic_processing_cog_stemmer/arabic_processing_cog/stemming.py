#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
created on 2014 Mar 28
by disooqi
'''
from . import script

class Stemmer:
   
    def __init__(self):
        pass

class Light10stemmer(Stemmer):
    larkey_defarticles = (u"ال", u"وال", u"بال", u"كال", u"فال", u"لل")
    larkey_suffixes = (u"ها", u"ان", u"ات", u"ون", u"ين", u"يه", u"ية", u"ه", u"ة", u"ي")

    def __init__(self):
        Stemmer.__init__(self)

    @staticmethod
    def stem_token(token):
        ''' The method takes a valid Arabic word as a parameter and return a stemmed term '''
        if not script.isArabicword(token):
            return token
        
        if len(token) > 3 and token[:1] == script.WAW:
            token = token[1:]
        length = 0
        wordlen = len(token)

        for article in Light10stemmer.larkey_defarticles:
            length = len(article)
            if (wordlen > length + 1) and (token[:length] == article):
                token = token[length:]
                break

        if len(token) > 2:
            wordlen = len(token)
            for suffix in Light10stemmer.larkey_suffixes:
                suflen = len(suffix)
                if (wordlen > len(suffix) + 1) and token.endswith(suffix):
                    token = token[:wordlen - suflen]
                    wordlen = len(token)

        return token





if __name__ == '__main__':
    pass


