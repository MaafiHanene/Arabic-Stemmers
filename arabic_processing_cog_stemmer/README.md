# ArabicProcessingCog 
A Python package that do stemming, tokenization, sentence breaking, segmentation, normalization, POS tagging for Arabic language.

- **Author/Affiliation**:  [Mohamed Eldesouki](https://mohamed-eldesouki.com/)
- **License**: [MIT License](https://github.com/disooqi/ArabicProcessingCog/blob/master/LICENSE)
- **Links**: [Github](https://github.com/disooqi/ArabicProcessingCog)


## Usage
### Python
#### Install
- You can download 'arabic_processing_cog' folder from [Here](https://github.com/disooqi/ArabicProcessingCog).
- Add 'arabic_processing_cog' folder to yout project root.

#### Run

```pyhton
from arabic_processing_cog.tokenization import ArabicTokenizer as arabic_tokenizer
from arabic_processing_cog.stemming import Light10stemmer as arabic_processing_cog_stemmer

string = 'مكتبة لمعالجة الكلمات العربية  وتجذيعها'
  for token in arabic_tokenizer.tokenize(string):
    stem_word = arabic_processing_cog_stemmer.stem_token(token)
    print(stem_word)
```


