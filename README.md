# Arabic-Stemmers

# Tashaphyne: Arabic Light Stemmer 
# تاشفين: التجذيع الخفيف للنصوص العربية   

 
| Programming Language    | Author/Affiliation | How to use ?                                        |
| --- | --- | --- | 
| Python         | Taha Zerrouki      | from tashaphyne.stemming import ArabicLightStemmer  |
|                |                    | arabic_light_stemmer = ArabicLightStemmer()         |
|                |                    | arabic_light_stemmer.light_stem(u"فسميتموها")               |
|                |                    | print arabic_light_stemmer.get_stem()               |

 [Tashaphyne](https://pypi.org/project/Tashaphyne/."Tashaphyne")
 
 # ISRI Arabic Stemmer
 
 
| Programming Language    | Author/Affiliation | How to use ?                                        |
| --- | --- | --- | 
| Python         | Hosam Algasaier    | from nltk.stem.isri import ISRIStemmer  |
|                |                    | isri_stemmer = ISRIStemmer()         |
|                |                    | stem_word = isri_stemmer.stem(u"فسميتموها")               |
|                |                    | print stem_word               |
 
 [ISRI Stemmer](https://www.nltk.org/_modules/nltk/stem/isri.html."ISRI Stemmer")
