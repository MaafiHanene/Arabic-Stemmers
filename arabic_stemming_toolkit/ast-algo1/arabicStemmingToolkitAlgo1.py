import os


class ArabicStemmingToolkitStemmerAlgo1():

    # Get the article content

    def readContent(article):

        if os.path.exists(article):
            return open(article, 'r', encoding="utf-8").read()

    def stem(self, content):

        jarASTalgo1 = os.path.join('.', 'AST1.jar')

        tmp = os.path.join('.', 'tmp')

        if os.path.exists(tmp):
            os.system('rm ' + tmp)

        open(tmp, 'w', encoding="utf-8").write(content)

        for folder, subs, files in os.walk(('.').encode( 'utf-8')):

                tmpStem = os.path.join('.', 'tmpStem.txt')

        if os.path.exists(tmpStem):
            os.system('rm ' + tmpStem)

        os.system('java -Dfile.encoding=UTF-8 -jar ' + jarASTalgo1 + ' ' + tmp +' '+ tmpStem)

        lines = self.readContent(tmpStem)

        os.system('rm ' + tmpStem)
        os.system('rm ' + tmp)

        words = lines.split()
        stems_list = []
        for word in words:
            # add new stem to dict
            stems_list.append(word)

        return stems_list

