# Tashaphyne    

#### Tashaphyne: Arabic Light Stemmer تاشفين: التجذيع الخفيف للنصوص العربية
Tashaphyne is an Arabic light stemmer and segmentor. It mainly supports light stemming (removing prefixes and suffixes) and give all possible segmentations. It use a modified finite state Automaton which allow to generate all segmentations.


|Features |   value
|---------|---------------------------------------------------------------------------------
|Author/Affiliation| [Taha Zerrouki](tahadz.com/."Taha_Zerrouki")|
|License|[GPL](https://github.com/linuxscout/tashaphyne/blob/master/LICENSE."GPL")|
|Source|[Github](https://github.com/linuxscout/tashaphyne/."tashaphyne")|
|Link|https://pypi.org/project/Tashaphyne/

## How to install ?
```
pip install tashaphyne
```

## How to run?:
```pyhton
from tashaphyne.stemming import ArabicLightStemmer
arabic_light_stemmer = ArabicLightStemmer()
arabic_light_stemmer.light_stem(u"فسميتموها")  
print arabic_light_stemmer.get_stem() 
```


