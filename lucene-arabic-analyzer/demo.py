from luceneArabicAnalyzerStemmer import LuceneArabicAnalyzerStemmer as lucene_arabic_analyzer_stemmer

string = u'مكتبة لمعالجة الكلمات العربية  وتجذيعها'

stems_list = lucene_arabic_analyzer_stemmer.stem(lucene_arabic_analyzer_stemmer, string)

file = open('output.txt', 'w+', encoding="utf-8")

for word in stems_list:
    file.write(word+'\n')

file.close()
