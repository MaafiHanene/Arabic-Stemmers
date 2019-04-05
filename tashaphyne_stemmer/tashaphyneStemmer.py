from tashaphyne.stemming import ArabicLightStemmer


def stem(string):

    # split given string into words
    words = string.split()
    stems_list = []

    arabic_light_stemmer = ArabicLightStemmer()

    for word in words:

        # stem word
        stem_word = arabic_light_stemmer.light_stem(word)
        # add new stem to dict
        stems_list.append(stem_word)

    return stems_list

