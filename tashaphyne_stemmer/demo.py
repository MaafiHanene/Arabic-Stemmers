import tashaphyneStemmer

string = u'مكتبة لمعالجة الكلمات العربية  وتجذيعها'

stems_dict = tashaphyneStemmer.stem(string)

file = open('output.txt', 'w+', encoding="utf-8")

for word in stems_dict:
    file.write(word+'\n')

file.close()
