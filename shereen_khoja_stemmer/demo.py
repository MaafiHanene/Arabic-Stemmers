from shereenKhojaStemmer import ShereenKhojaStemmer as shereen_khoja_stemmer

string = 'مكتبة لمعالجة الكلمات العربية  وتجذيعها'

stems_list = shereen_khoja_stemmer.stem(shereen_khoja_stemmer, string)

file = open('output.txt', 'w+', encoding="utf-8")

for word in stems_list:
    file.write(word+'\n')

file.close()
