#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
created on 2014 Mar 28
by disooqi
'''
import script

def break_into_sentences(paragraph):
    sentences = list()
    temp_sentence = list()
    flag = False
    for ch in paragraph.strip():
        if ch in [u'؟', u'!', u'.', u':', u'؛']:
            flag = True
        elif flag:
            sentences.append(''.join(temp_sentence).strip())
            temp_sentence = []
            flag = False
            
        temp_sentence.append(ch)

    else:
        sentences.append(''.join(temp_sentence).strip())
        return sentences

if __name__ == '__main__':
    pass

