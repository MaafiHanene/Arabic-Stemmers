from arabicStemmingToolkitAlgo2 import ArabicStemmingToolkitStemmerAlgo2 as ast_algo2_stemmer

string = 'مكتبة لمعالجة الكلمات العربية  وتجذيعها'

stems_list = ast_algo2_stemmer.stem(ast_algo2_stemmer, string)

file = open('output.txt', 'w+', encoding="utf-8")

for word in stems_list:
    file.write(word+'\n')

file.close()
