# Tashaphyne (Arabic Light Stemmer)  
Tashaphyne is an Arabic light stemmer and segmentor. It mainly supports light stemming (removing prefixes and suffixes) and give all possible segmentations. It use a modified finite state Automaton which allow to generate all segmentations.

- **Author/Affiliation**:  [Taha Zerrouki](tahadz.com/."Taha_Zerrouki")
- **License**: [GPL](https://github.com/linuxscout/tashaphyne/blob/master/LICENSE."GPL")
- **Links**: [Github](https://github.com/linuxscout/tashaphyne/)

## How to install
```shell
 pip install tashaphyne
```

## How to run
### Python
```pyhton
from tashaphyne.stemming import ArabicLightStemmer

arabic_light_stemmer = ArabicLightStemmer()
arabic_light_stemmer.light_stem(u"فسميتموها")  
print(arabic_light_stemmer.get_stem())

```


