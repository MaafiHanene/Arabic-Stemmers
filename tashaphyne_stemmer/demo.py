import tashaphyneStemmer

string = u'مكتبة لمعالجة الكلمات العربية  وتجذيعها'

stems_dict = tashaphyneStemmer.stem(string)

file = open('test_words.txt', 'w+', encoding="utf-8")

for word_count in stems_dict:
    file.write(stems_dict[word_count]+'\n')

file.close()
