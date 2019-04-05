import os


class FarasaStemmer():

    # Get the article content

    def readContent(article):

        if os.path.exists(article):
            return open(article, 'r', encoding="utf-8").read()

    def stem(self, content):

        jarFarasaSegmenter = os.path.join('.', 'FarasaSegmenterJar.jar')

        tmp = os.path.join('.', 'tmp')

        if os.path.exists(tmp):
            os.system('rm ' + tmp)

        open(tmp, 'w', encoding="utf-8").write(content)

        for folder, subs, files in os.walk(('.').encode( 'utf-8')):

                tmpLemma = os.path.join('.', 'tmpLemma.txt')

        if os.path.exists(tmpLemma):
            os.system('rm ' + tmpLemma)

        os.system('java -Dfile.encoding=UTF-8 -jar ' + jarFarasaSegmenter + ' -l true -i ' + tmp + ' -o ' + tmpLemma)

        string = self.readContent(tmpLemma)

        os.system('rm ' + tmpLemma)
        os.system('rm ' + tmp)

        words = string.split()
        stems_dict = []
        for word in words:
            # add new stem to dict
            stems_dict.append(word)

        return stems_dict

