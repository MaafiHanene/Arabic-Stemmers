import requests
from bs4 import BeautifulSoup


def stem(string):

    # split given string into words
    words = string.split()
    stems_list = []

    for word in words:

        # Send POST request to Alkhalil API
        response = requests.post("http://toolkit.oujda-nlp-team.net/AlKhalil2/ResponseWords.php", data={'words': word})
        # HTML Parser
        response_text = BeautifulSoup(response.text, features="html.parser")

        try:
            for stem_word in response_text.find_all('font')[1]:
                stems_list.append(stem_word)

        # word to stem not found
        except IndexError:
            # return origin word without stemming
            stems_list.append(word)

    return stems_list






