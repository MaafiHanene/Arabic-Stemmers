from arabicStemmingToolkitAlgo3 import ArabicStemmingToolkitStemmerAlgo3 as ast_algo3_stemmer

string = 'مكتبة لمعالجة الكلمات العربية  وتجذيعها'

stems_list = ast_algo3_stemmer.stem(ast_algo3_stemmer, string)

file = open('output.txt', 'w+', encoding="utf-8")

for word in stems_list:
    file.write(word+'\n')

file.close()
