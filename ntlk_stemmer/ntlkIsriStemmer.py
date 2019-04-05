from nltk.stem.isri import ISRIStemmer


def stem(string):

    # split given string into words
    words = string.split()
    stems_dict = []

    isri_stemmer = ISRIStemmer()

    for word in words:
        # stem word
        stem_word = isri_stemmer.stem(word)
        # add new stem to dict
        stems_dict.append(stem_word)

    return stems_dict

