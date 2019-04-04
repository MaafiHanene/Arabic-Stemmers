from nltk.stem.isri import ISRIStemmer


def stem(string):

    # split given string into words
    words = string.split()
    stems_dict = {}
    count = 0

    isri_stemmer = ISRIStemmer()


    for word in words:
        word_count = 'word'+str(count)
        # stem word
        stem_word = isri_stemmer.stem(word)
        # add new stem to dict
        stems_dict[word_count] = stem_word
        count = count + 1

    return stems_dict

