from snowballstemmer import stemmer


def stem(string):

    # split given string into words
    words = string.split()
    stems_list = []

    assems_arabic_light_stemmer = stemmer("arabic")

    for word in words:
        # stem word
        stem_word = assems_arabic_light_stemmer.stemWord(word)
        # add new stem to dict
        stems_list.append(stem_word)

    return stems_list
