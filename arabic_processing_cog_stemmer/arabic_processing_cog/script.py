#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
created on 2014 Mar 28
by disooqi
'''
import re

SPACE            = u'\u0020'
EXCLAMATION      = u'\u0021'
en_QUOTATION     = u'\u0022'
NUMBER_SIGN      = u'\u0023'
DOLLAR_SIGN      = u'\u0024'
en_PERCENT       = u'\u0025' #unichr(37)
AMPERSAND        = u'\u0026'
APOSTROPHE       = u'\u0027' #unichr(39)
LEFT_PARENTHESIS = u'\u0028'
RIGHT_PARENTHESIS= u'\u0029'
ASTERISK         = u'\u002a' #unichr(42)
PLUS_SIGN        = u'\u002b'
en_COMMA         = u'\u002c'
HYPHEN_MINUS     = u'\u002d' #unichr(45)
en_FULL_STOP     = u'\u002e'
SLASH            = u'\u002f'
# English Numbers
ZERO             = u'\u0030'
ONE              = u'\u0031'
TWO              = u'\u0032'
THREE            = u'\u0033'
FOUR             = u'\u0034'
FIVE             = u'\u0035'
SIX              = u'\u0036'
SEVEN            = u'\u0037'
EIGHT            = u'\u0038'
NINE             = u'\u0039'

en_COLON             = u'\u003a' #unichr(58)
en_SEMICOLON         = u'\u003b' 
en_LESS_THAN         = u'\u003c' #unichr(60)
en_EQUALS_SIGN       = u'\u003d' #
en_GREATER_THAN      = u'\u003e' #
en_QUESTION          = u'\u003f'
COMMERCIAL_AT        = u'\u0040'

LEFT_SQUARE_BRACKET  = u'\u005b'
BACKSLASH            = u'\u005c'
RIGHT_SQUARE_BRACKET = u'\u005d'
CIRCUMFLEX_ACCENT    = u'\u005e'
UNDERSCORE           = u'\u005f'
GRAVE_ACCENT         = u'\u0060'

LEFT_CURLY_BRACKET   = u'\u007b'
VERTICAL_LINE        = u'\u007c'
RIGHT_CURLY_BRACKET  = u'\u007d'
TILDE                = u'\u007e'

Leftpointing_double_angle_quotation_mark  = u'\u00ab'
MIDDLE_DOT                                = u'\u00b7' #unichr(183)
Rightpointing_double_angle_quotation_mark = u'\u00bb'

ar_COMMA         = u'\u060c'
ar_DATE_SEPARATO = u'\u060d'
ar_SEMICOLON     = u'\u061b'
ar_QUESTION      = u'\u061f' #QUESTION
HAMZA            = u'\u0621'
ALEF_MADDA       = u'\u0622'
ALEF_HAMZA_ABOVE = u'\u0623'
WAW_HAMZA        = u'\u0624'
ALEF_HAMZA_BELOW = u'\u0625'
YEH_HAMZA        = u'\u0626'
ALEF             = u'\u0627'
BEH              = u'\u0628'
TEH_MARBUTA      = u'\u0629'
TEH              = u'\u062a'
THEH             = u'\u062b'
JEEM             = u'\u062c'
HAH              = u'\u062d'
KHAH             = u'\u062e'
DAL              = u'\u062f'
THAL             = u'\u0630'
REH              = u'\u0631'
ZAIN             = u'\u0632'
SEEN             = u'\u0633'
SHEEN            = u'\u0634'
SAD              = u'\u0635'
DAD              = u'\u0636'
TAH              = u'\u0637'
ZAH              = u'\u0638'
AIN              = u'\u0639'
GHAIN            = u'\u063a'
TATWEEL          = u'\u0640'
FEH              = u'\u0641'
QAF              = u'\u0642'
KAF              = u'\u0643'
LAM              = u'\u0644'
MEEM             = u'\u0645'
NOON             = u'\u0646'
HEH              = u'\u0647'
WAW              = u'\u0648'
ALEF_MAKSURA     = u'\u0649'
YEH              = u'\u064a'
MADDA_ABOVE      = u'\u0653'
HAMZA_ABOVE      = u'\u0654'
HAMZA_BELOW      = u'\u0655'

ar_ZERO          = u'\u0660'
ar_ONE           = u'\u0661'
ar_TWO           = u'\u0662'
ar_THREE         = u'\u0663'
ar_FOUR          = u'\u0664'
ar_FIVE          = u'\u0665'
ar_SIX           = u'\u0666'
ar_SEVEN         = u'\u0667'
ar_EIGHT         = u'\u0668'
ar_NINE          = u'\u0669'

ar_PERCENT       = u'\u066a' #PERCENT 
ar_DECIMAL       = u'\u066b'
ar_THOUSANDS     = u'\u066c'
ar_STAR          = u'\u066d'
MINI_ALEF        = u'\u0670'
ALEF_WASLA       = u'\u0671'
ar_FULL_STOP     = u'\u06d4' #FULL_STOP
BYTE_ORDER_MARK  = u'\ufeff'

# Diacritics
FATHATAN         = u'\u064b'
DAMMATAN         = u'\u064c'
KASRATAN         = u'\u064d'
FATHA            = u'\u064e'
DAMMA            = u'\u064f'
KASRA            = u'\u0650'
SHADDA           = u'\u0651'
SUKUN            = u'\u0652'

# Small Letters
SMALL_ALEF      =u"\u0670"
SMALL_WAW       =u"\u06E5"
SMALL_YEH       =u"\u06E6"
#Ligatures
LAM_ALEF                    =u'\ufefb'
LAM_ALEF_HAMZA_ABOVE        =u'\ufef7'
LAM_ALEF_HAMZA_BELOW        =u'\ufef9'
LAM_ALEF_MADDA_ABOVE        =u'\ufef5'
simple_LAM_ALEF             =u'\u0644\u0627'
simple_LAM_ALEF_HAMZA_ABOVE =u'\u0644\u0623'
simple_LAM_ALEF_HAMZA_BELOW =u'\u0644\u0625'
simple_LAM_ALEF_MADDA_ABOVE =u'\u0644\u0622'

Left_double_quotation_mark  = u'\u201c' #unichr(8220)
Right_double_quotation_mark = u'\u201d' #unichr(8221)
BULLET                      = u'\u2022'

# groups
LETTERS=u''.join([
        ALEF , BEH , TEH  , TEH_MARBUTA  , THEH  , JEEM  , HAH , KHAH ,
        DAL   , THAL  , REH   , ZAIN  , SEEN   , SHEEN  , SAD , DAD , TAH   , ZAH   ,
        AIN   , GHAIN   , FEH  , QAF , KAF , LAM , MEEM , NOON, HEH , WAW, YEH  ,
        HAMZA  ,  ALEF_MADDA , ALEF_HAMZA_ABOVE , WAW_HAMZA   , ALEF_HAMZA_BELOW  , YEH_HAMZA  ,
        ])

TASHKEEL =(FATHATAN, DAMMATAN, KASRATAN,
            FATHA,DAMMA,KASRA,
            SUKUN,
            SHADDA);
HARAKAT =(  FATHATAN,   DAMMATAN,   KASRATAN,
            FATHA,  DAMMA,  KASRA,
            SUKUN
            );
SHORTHARAKAT =( FATHA,  DAMMA,  KASRA, SUKUN);

TANWIN =(FATHATAN,  DAMMATAN,   KASRATAN);


LIGUATURES=(
            LAM_ALEF,
            LAM_ALEF_HAMZA_ABOVE,
            LAM_ALEF_HAMZA_BELOW,
            LAM_ALEF_MADDA_ABOVE,
            );
HAMZAT=(
            HAMZA,
            WAW_HAMZA,
            YEH_HAMZA,
            HAMZA_ABOVE,
            HAMZA_BELOW,
            ALEF_HAMZA_BELOW,
            ALEF_HAMZA_ABOVE,
            );
ALEFAT=(
            ALEF,
            ALEF_MADDA,
            ALEF_HAMZA_ABOVE,
            ALEF_HAMZA_BELOW,
            ALEF_WASLA,
            ALEF_MAKSURA,
            SMALL_ALEF,

        );
WEAK   = ( ALEF, WAW, YEH, ALEF_MAKSURA);
YEHLIKE= ( YEH,  YEH_HAMZA,  ALEF_MAKSURA,   SMALL_YEH  );

WAWLIKE     =   ( WAW,  WAW_HAMZA,  SMALL_WAW );
TEHLIKE     =   ( TEH,  TEH_MARBUTA );

SMALL   =( SMALL_ALEF, SMALL_WAW, SMALL_YEH)
MOON =(HAMZA            ,
        ALEF_MADDA       ,
        ALEF_HAMZA_ABOVE ,
        ALEF_HAMZA_BELOW ,
        ALEF             ,
        BEH              ,
        JEEM             ,
        HAH              ,
        KHAH             ,
        AIN              ,
        GHAIN            ,
        FEH              ,
        QAF              ,
        KAF              ,
        MEEM             ,
        HEH              ,
        WAW              ,
        YEH
    );
SUN=(
        TEH              ,
        THEH             ,
        DAL              ,
        THAL             ,
        REH              ,
        ZAIN             ,
        SEEN             ,
        SHEEN            ,
        SAD              ,
        DAD              ,
        TAH              ,
        ZAH              ,
        LAM              ,
        NOON             ,
    );
AlphabeticOrder={
                ALEF             : 1,
                BEH              : 2,
                TEH              : 3,
                TEH_MARBUTA      : 3,
                THEH             : 4,
                JEEM             : 5,
                HAH              : 6,
                KHAH             : 7,
                DAL              : 8,
                THAL             : 9,
                REH              : 10,
                ZAIN             : 11,
                SEEN             : 12,
                SHEEN            : 13,
                SAD              : 14,
                DAD              : 15,
                TAH              : 16,
                ZAH              : 17,
                AIN              : 18,
                GHAIN            : 19,
                FEH              : 20,
                QAF              : 21,
                KAF              : 22,
                LAM              : 23,
                MEEM             : 24,
                NOON             : 25,
                HEH              : 26,
                WAW              : 27,
                YEH              : 28,
                HAMZA            : 29,

                ALEF_MADDA       : 29,
                ALEF_HAMZA_ABOVE : 29,
                WAW_HAMZA        : 29,
                ALEF_HAMZA_BELOW : 29,
                YEH_HAMZA        : 29,
                }
NAMES ={
                ALEF             :  u"ألف",
                BEH              : u"باء",
                TEH              : u'تاء' ,
                TEH_MARBUTA      : u'تاء مربوطة' ,
                THEH             : u'ثاء' ,
                JEEM             : u'جيم' ,
                HAH              : u'حاء' ,
                KHAH             : u'خاء' ,
                DAL              : u'دال' ,
                THAL             : u'ذال' ,
                REH              : u'راء' ,
                ZAIN             : u'زاي' ,
                SEEN             : u'سين' ,
                SHEEN            : u'شين' ,
                SAD              : u'صاد' ,
                DAD              : u'ضاد' ,
                TAH              : u'طاء' ,
                ZAH              : u'ظاء' ,
                AIN              : u'عين' ,
                GHAIN            : u'غين' ,
                FEH              : u'فاء' ,
                QAF              : u'قاف' ,
                KAF              : u'كاف' ,
                LAM              : u'لام' ,
                MEEM             : u'ميم' ,
                NOON             : u'نون' ,
                HEH              : u'هاء' ,
                WAW              : u'واو' ,
                YEH              : u'ياء' ,
                HAMZA            : u'همزة' ,

                TATWEEL          : u'تطويل' ,
                ALEF_MADDA       : u'ألف ممدودة' ,
                ALEF_MAKSURA      : u'ألف مقصورة' ,
                ALEF_HAMZA_ABOVE : u'همزة على الألف' ,
                WAW_HAMZA        : u'همزة على الواو' ,
                ALEF_HAMZA_BELOW : u'همزة تحت الألف' ,
                YEH_HAMZA        : u'همزة على الياء' ,
                FATHATAN         : u'فتحتان',
                DAMMATAN         : u'ضمتان',
                KASRATAN         : u'كسرتان',
                FATHA            : u'فتحة',
                DAMMA            : u'ضمة',
                KASRA            : u'كسرة',
                SHADDA           : u'شدة',
                SUKUN            : u'سكون',
                }
#!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
PUNCTUATIONS = (ar_COMMA, ar_SEMICOLON, ar_QUESTION, ar_PERCENT, ar_DECIMAL,
                ar_THOUSANDS, ar_FULL_STOP,
                
                EXCLAMATION, en_QUOTATION, NUMBER_SIGN, DOLLAR_SIGN, en_PERCENT,
                AMPERSAND, LEFT_PARENTHESIS, RIGHT_PARENTHESIS,
                ASTERISK, PLUS_SIGN, en_COMMA, HYPHEN_MINUS, en_FULL_STOP,
                SLASH, en_COLON, en_SEMICOLON, en_LESS_THAN, en_EQUALS_SIGN,
                en_GREATER_THAN, en_QUESTION, COMMERCIAL_AT, LEFT_SQUARE_BRACKET,
                BACKSLASH, RIGHT_SQUARE_BRACKET, CIRCUMFLEX_ACCENT, UNDERSCORE,
                GRAVE_ACCENT, LEFT_CURLY_BRACKET, VERTICAL_LINE,
                RIGHT_CURLY_BRACKET, TILDE, Leftpointing_double_angle_quotation_mark,
                MIDDLE_DOT, Rightpointing_double_angle_quotation_mark ) #APOSTROPHE

##
##punc_to_remove = (ar_COMMA, ar_SEMICOLON, ar_QUESTION, ar_PERCENT, ar_DECIMAL,
##                  ar_THOUSANDS, ar_FULL_STOP, EXCLAMATION, en_QUOTATION, NUMBER_SIGN,
##                  DOLLAR_SIGN, en_PERCENT,
##                  AMPERSAND, APOSTROPHE, LEFT_PARENTHESIS, RIGHT_PARENTHESIS,
##                  ASTERISK, PLUS_SIGN, en_COMMA, HYPHEN_MINUS, en_FULL_STOP,
##                  SLASH, en_COLON, en_SEMICOLON, en_LESS_THAN, en_EQUALS_SIGN,
##                  en_GREATER_THAN, en_QUESTION, COMMERCIAL_AT, LEFT_SQUARE_BRACKET,
##                  BACKSLASH, RIGHT_SQUARE_BRACKET, CIRCUMFLEX_ACCENT, UNDERSCORE,
##                  GRAVE_ACCENT, LEFT_CURLY_BRACKET, VERTICAL_LINE,
##                  RIGHT_CURLY_BRACKET, TILDE)

def isHaraka(archar):
    """Checks for Arabic Harakat Marks (FATHA,DAMMA,KASRA,SUKUN,TANWIN).
    @param archar: arabic unicode char
    @type archar: unicode
    """
    if archar in HARAKAT:
        return True;
    else: return False;

def isArabicword(word):
    """ Checks for an valid Arabic  word.
    An Arabic word not contains spaces, digits and pounctuation
    avoid some spelling error,  TEH_MARBUTA must be at the end.
    @param word: input word
    @type word: unicode
    @return: True if all charaters are in Arabic block
    @rtype: Boolean
    """
    if len(word)==0 : return False;
    elif re.search(u"([^\u0600-\u0652%s%s%s])"%(LAM_ALEF, LAM_ALEF_HAMZA_ABOVE,LAM_ALEF_MADDA_ABOVE),word):
        return False;
    elif isHaraka(word[0]) or word[0] in (WAW_HAMZA,YEH_HAMZA):
        return False;
#  if Teh Marbuta or Alef_Maksura not in the end
    elif re.match(u"^(.)*[%s](.)+$"%ALEF_MAKSURA,word):
        return False;
    elif re.match(u"^(.)*[%s]([^%s%s%s])(.)+$"%(TEH_MARBUTA,DAMMA,KASRA,FATHA),word):
        return False;
    else:
        return True;




if __name__ == '__main__':
    pass






























































