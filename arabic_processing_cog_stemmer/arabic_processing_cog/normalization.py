#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
created on 2014 Mar 28
by disooqi
'''
from . import config
from .script import *

#:)
class Arabic_normalization:
    #this is a class variable
    
    norm_table = {  ALEF_MADDA:ALEF,
                    ALEF_HAMZA_ABOVE:ALEF,
                    ALEF_HAMZA_BELOW:ALEF,
                    
                    TEH_MARBUTA:HEH,
                    ALEF_MAKSURA:YEH,

                    TATWEEL:u'',

                    #Ligatures
                    LAM_ALEF:LAM+ALEF,
                    LAM_ALEF_HAMZA_ABOVE:LAM+ALEF,
                    LAM_ALEF_HAMZA_BELOW:LAM+ALEF,
                    LAM_ALEF_MADDA_ABOVE:LAM+ALEF,
                    
                    #Diacritics
                    FATHATAN:u'',            DAMMATAN:u'',
                    KASRATAN:u'',            FATHA:u'',
                    DAMMA:u'',               KASRA:u'',
                    SHADDA:u'',              SUKUN:u'',

                    #Numbers
                    ZERO:ar_ZERO,
                    ONE:ar_ONE,
                    TWO:ar_TWO,
                    THREE:ar_THREE,
                    FOUR:ar_FOUR,
                    FIVE:ar_FIVE,
                    SIX:ar_SIX,
                    SEVEN:ar_SEVEN,
                    EIGHT:ar_EIGHT,
                    NINE:ar_NINE,                    
                    }


    punctuation_norm_table = {
        en_QUESTION:ar_QUESTION,
        en_SEMICOLON:ar_SEMICOLON,
        en_COMMA:ar_COMMA,
        en_FULL_STOP:ar_FULL_STOP,
        en_PERCENT:ar_PERCENT,
        ar_DECIMAL:ar_DECIMAL,
        EXCLAMATION:EXCLAMATION,
        
        Leftpointing_double_angle_quotation_mark:en_QUOTATION,
        Rightpointing_double_angle_quotation_mark:en_QUOTATION,
        Left_double_quotation_mark:en_QUOTATION,
        Right_double_quotation_mark:en_QUOTATION,
##        en_Less_than:en_QUOTATION,
##        en_Greater_than:en_QUOTATION,
        ar_STAR:u'',
        ASTERISK:u'',
        BULLET:u'',
        en_EQUALS_SIGN:u'',
        MIDDLE_DOT:ar_FULL_STOP,
        }
    
    
    #constructor method
    def __init__(self):
        # Any thing after 'self.' is an attribute of the "object"
        #self.y = x

        #this is how to access the class variable inside the class
        Arabic_normalization.variable += 1

        #this a wrong way to access the class variable
        # variable += 1

    def __str__(self):
        return 'trying'

    def __del__(self):
        pass

    #class method (also, static method), i.e. accessed using class name
    # not the object    
    @staticmethod
    def normalize_sentence(line):
        if config.Add_SPACE_after_TEH_MARBUTA:
            line = line.replace(TEH_MARBUTA, TEH_MARBUTA+SPACE)

        #if config.isolate_punc:
        for ch in PUNCTUATIONS:
            if config.remove_punc:
                line = line.replace(ch, SPACE)
                continue
                
            if config.isolate_punc:
                line = line.replace(ch, SPACE+ch+SPACE)    
            
            if config.replace_punc:
                tempch = Arabic_normalization.punctuation_norm_table.get(ch, ch)
                line = line.replace(ch, tempch)
            
        tokens = line.strip().split()

        if config.ignore_oneword_line and len(tokens)==1:
            return ''
        
        terms = list()
        for token in tokens[:]:
            term = Arabic_normalization.normalize_token(token)
            if term.strip():
                terms.append(term)

        return ' '.join(terms)


    #you could use the following line instead of @staticmethod decorator
    #normalize_line = staticmethod(normalize_line)
    @staticmethod
    def normalize_token(token):
        ''' a token could be a single word, a multiword expression, or a named entity '''
        # check if token is a valid Arabic Word (from Taha Zerrouki)
        if not isArabicword(token):
            if config.remove_nonArabic_word:
                return ''
            elif not config.process_nonArabic_word:
                return token

        if config.tweet_normalization:
            token = re.sub(r'(.)\1+', r'\1\1', token)

        term = list()
        for char in token:
            if char==ALEF_HAMZA_ABOVE and not config.replace_ALEF_HAMZA_ABOVE:
                term.append(char)
            elif char==ALEF_HAMZA_BELOW and not config.replace_ALEF_HAMZA_BELOW:
                term.append(char)
            elif char==ALEF_MADDA and not config.replace_ALEF_MADDA:
                term.append(char)
            elif char==ALEF_MAKSURA and not config.replace_ALEF_MAKSURA:
                term.append(char)
            elif char==TEH_MARBUTA and not config.replace_TEH_MARBUTA:
                term.append(char)
            elif char==TATWEEL and not config.remove_KASHIDA:
                term.append(char)
            elif char in TASHKEEL and not config.remove_diacritics:
                term.append(char)
            else:
                term.append(Arabic_normalization.norm_table.get(char, char))

        # return ''.join(term)
        # if term[0] == 'و':
        #     return ''.join(term[1:])

        return ''.join(term)

    
        
if __name__ == '__main__':
    pass

    #this is how to access the class variable outside the class
    #print Arabic_normalization.variable

    #accesing the class method
    #print Arabic_normalization.getVariable()

























    
