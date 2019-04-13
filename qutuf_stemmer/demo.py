import qutufStemmer

string = 'السلام عليكم'

stems_list = qutufStemmer.stem(string)

file = open('output.txt', 'w+', encoding="utf-8")

for word in stems_list:
    file.write(word+'\n')

file.close()
