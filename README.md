# Arabic-Stemmers

# Al Khalil Morpho Sys Stemmer
 
 [Al Khalil Stemmer](http://oujda-nlp-team.net/en/."AlKalilStemmer")
 
 ### Requirements:

 requests package : https://pypi.org/project/requests/
 beautifulsoup4 package: https://pypi.org/project/beautifulsoup4/

```pyhton
 # -*- coding: utf-8 -*-
import alkhalilMorphoSysStemmer

# unicode input
string = 'مكتبة لمعالجة الكلمات العربية  وتجذيعها'
# return an array
stems_list = alkhalilMorphoSysStemmer.stem(string)
```

# Arabic-Stemming-Toolkit AST (Three (3) stemming algorithms)
 
 [AST](https://github.com/mhmdio/Arabic-Stemming-Toolkit."AST")
 
 ### Requirements:

Java Runtime Envionment (JRE)

##### Algorithm 1
```pyhton
 # -*- coding: utf-8 -*-

from arabicStemmingToolkitAlgo1 import ArabicStemmingToolkitStemmerAlgo1 as ast_algo1_stemmer

# unicode input
string = 'مكتبة لمعالجة الكلمات العربية  وتجذيعها'
# return an array
stems_list = ast_algo1_stemmer.stem(ast_algo1_stemmer, string)
```

##### Algorithm 2
```pyhton
 # -*- coding: utf-8 -*-

from arabicStemmingToolkitAlgo2 import ArabicStemmingToolkitStemmerAlgo2 as ast_algo2_stemmer

# unicode input
string = 'مكتبة لمعالجة الكلمات العربية  وتجذيعها'
# return an array
stems_list = ast_algo2_stemmer.stem(ast_algo2_stemmer, string)
```

##### Algorithm 3
```pyhton
 # -*- coding: utf-8 -*-

from arabicStemmingToolkitAlgo3 import ArabicStemmingToolkitStemmerAlgo3 as ast_algo3_stemmer

# unicode input
string = 'مكتبة لمعالجة الكلمات العربية  وتجذيعها'
# return an array
stems_list = ast_algo3_stemmer.stem(ast_algo3_stemmer, string)
```

# ArabicProcessingCog 

 [ArabicProcessingCog](https://github.com/disooqi/ArabicProcessingCog."ArabicProcessingCog")

 ```pyhton
 # -*- coding: utf-8 -*-
 
import arabicProcessingCogStemmer

string = 'مكتبة لمعالجة الكلمات العربية  وتجذيعها'
# return an array
stems_list = arabicProcessingCogStemmer.stem(string)
```

# Assem's Arabic Light Stemmer 

 [Assem's stemmer](https://www.arabicstemmer.com/."AssemsStemmer")
 
 ### Requirements:
 
 snowballStemmer : https://www.arabicstemmer.com/python
 
 ```pyhton
 # -*- coding: utf-8 -*-
 
import assemsArabicLightStemmer

# unicode input
string = u'مكتبة لمعالجة الكلمات العربية  وتجذيعها'
# return an array
stems_list = assemsArabicLightStemmer.stem(string)
```

# FARASA
 
 [farasa](http://qatsdemo.cloudapp.net/farasa/demo.html."farasa")
 
 ### Requirements:

Java Runtime Envionment (JRE)

```pyhton
 # -*- coding: utf-8 -*-

from farasaStemmer import FarasaStemmer as farasa_stemmer

# unicode input
string = u'مكتبة لمعالجة الكلمات العربية  وتجذيعها'
# return an array
stems_list = farasa_stemmer.stem(farasa_stemmer, string)
```

# lucene-arabic-analyzer
 
 [lucene-arabic-analyzer](https://github.com/msarhan/lucene-arabic-analyzer."lucene-arabic-analyzer")
 
 ### Requirements:

Java Runtime Envionment (JRE)

```pyhton
 # -*- coding: utf-8 -*-

from luceneArabicAnalyzerStemmer import LuceneArabicAnalyzerStemmer as lucene_arabic_analyzer_stemmer

# unicode input
string = u'مكتبة لمعالجة الكلمات العربية  وتجذيعها'
# return an array
stems_list = lucene_arabic_analyzer_stemmer.stem(lucene_arabic_analyzer_stemmer, string)
```

# Natural Language Toolkit: The ISRI Arabic Stemmer
 
 [ISRI Stemmer](https://www.nltk.org/_modules/nltk/stem/isri.html."ISRIStemmer")
 
 ### Requirements:
 
nltk package : https://pypi.org/project/nltk/

```pyhton
 # -*- coding: utf-8 -*-

import ntlkIsriStemmer

# unicode input
string = u'مكتبة لمعالجة الكلمات العربية  وتجذيعها'
# return an array
stems_list = ntlkIsriStemmer.stem(string)
```

# Qutuf (قُطُوْف) 

 [Qutuf](https://github.com/Qutuf/Qutuf."Qutuf")
 
 ### Requirements:
 
 requests package : https://pypi.org/project/requests/
 
 ```pyhton
 # -*- coding: utf-8 -*-
 
import qutufStemmer

# unicode input
string = 'السلام عليكم'
# return an array
stems_list = qutufStemmer.stem(string)
```

# Shereene Khoja Stemmer
 
 ### Requirements:

Java Runtime Envionment (JRE)

```pyhton
 # -*- coding: utf-8 -*-

from shereenKhojaStemmer import ShereenKhojaStemmer as shereen_khoja_stemmer

# unicode input
string = 'مكتبة لمعالجة الكلمات العربية  وتجذيعها'
# return an array
stems_list = shereen_khoja_stemmer.stem(shereen_khoja_stemmer, string)
```

# Tashaphyne: Arabic Light Stemmer 

 [Tashaphyne](https://pypi.org/project/Tashaphyne/."Tashaphyne")
 
 ### Requirements:
 
 Tashaphyne package : https://pypi.org/project/Tashaphyne/
 
 ```pyhton
 # -*- coding: utf-8 -*-
 
import tashaphyneStemmer

# unicode input
string = u'مكتبة لمعالجة الكلمات العربية  وتجذيعها'
# return an array
stems_list = tashaphyneStemmer.stem(string)
```
 
 
