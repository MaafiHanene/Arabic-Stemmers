from tashaphyne.stemming import ArabicLightStemmer


def stem(string):

    # split given string into words
    words = string.split()
    arabic_light_stemmer = ArabicLightStemmer()
    stems_dict = {}
    count = 0

    for word in words:
        word_count = 'word'+str(count)
        # stem word
        stem_word = arabic_light_stemmer.light_stem(word)
        # add new stem to dict
        stems_dict[word_count] = stem_word
        count = count + 1

    return stems_dict

