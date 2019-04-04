import ntlkIsriStemmer

string = u'مكتبة لمعالجة الكلمات العربية  وتجذيعها'

stems_dict = ntlkIsriStemmer.stem(string)

file = open('output.txt', 'w+', encoding="utf-8")

for word_count in stems_dict:
    file.write(stems_dict[word_count]+'\n')

file.close()
