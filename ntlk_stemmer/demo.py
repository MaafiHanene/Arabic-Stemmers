import ntlkIsriStemmer

string = u'مكتبة لمعالجة الكلمات العربية  وتجذيعها'

stems_list = ntlkIsriStemmer.stem(string)

file = open('output.txt', 'w+', encoding="utf-8")

for word in stems_list:
    file.write(word+'\n')

file.close()
