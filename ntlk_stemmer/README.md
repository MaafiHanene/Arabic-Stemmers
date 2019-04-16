# ISRI Arabic Stemmer  
ISRI Arabic stemmer based on algorithm: Arabic Stemming without a root dictionary. Information Science Research Institute. University of Nevada, Las Vegas, USA.

- **Author/Affiliation**:  Hosam Algasaier
- **License**: /
- **Links**: [Website](https://www.nltk.org/_modules/nltk/stem/isri.html)


## Usage
### Python
#### Install
```shell
 pip install ntlk
```

#### Run

```pyhton
from nltk.stem.isri import ISRIStemmer

isri_stemmer = ISRIStemmer()
stem_word = isri_stemmer.stem(u"فسميتموها")
print(stem_word)
```


