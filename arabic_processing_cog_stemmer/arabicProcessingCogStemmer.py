from arabic_processing_cog.tokenization import ArabicTokenizer as arabic_tokenizer
from arabic_processing_cog.stemming import Light10stemmer as arabic_processing_cog_stemmer


def stem(string):

    stems_dict = []
    # split given string into words (tokens) using ArabicTokenizer
    for token in arabic_tokenizer.tokenize(string):
        stem_word = arabic_processing_cog_stemmer.stem_token(token)
        stems_dict.append(stem_word)

    return stems_dict
