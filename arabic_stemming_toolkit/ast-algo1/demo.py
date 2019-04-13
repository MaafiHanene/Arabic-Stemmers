from arabicStemmingToolkitAlgo1 import ArabicStemmingToolkitStemmerAlgo1 as ast_algo1_stemmer

string = 'مكتبة لمعالجة الكلمات العربية  وتجذيعها'

stems_list = ast_algo1_stemmer.stem(ast_algo1_stemmer, string)

file = open('output.txt', 'w+', encoding="utf-8")

for word in stems_list:
    file.write(word+'\n')

file.close()
