import requests as reqs


def stem(string):

    # split given string into words
    words = string.split()
    stems_list = []

    for word in words:

        # Get Request
        url = "https://qutuf.herokuapp.com/?functionality=lemma&outputformat=json&text="+word
        response = reqs.get(url)
        data = response.json()

        first_word = data.get("Text").get("Sentence").get("Word")[0]
        if first_word.get("@has_been_identified")=='true':
            stem_word= first_word.get("@lemmas")
        else:
            # no result, return origin word (without stemming)
            stem_word = word

        stems_list.append(stem_word)

    return stems_list
