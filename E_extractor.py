import re
import docx
import os


def extractor(folder_path):
    # this function matches all email formats
    def readtextdoc(path):
        doc = docx.Document(path)

        completedText = []

        for paragraph in doc.paragraphs:
            completedText.append(paragraph.text)

        return "\n".join(completedText)

    text = readtextdoc(folder_path)

    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+')

    matches = pattern.finditer(text)

    def first_match(matches):
        ma = 1
        for i in matches:
            if ma < 2:
                print(i.group(0))
                ma += 1
                return i

    ans = str(first_match(matches).group(0))
    return ans + ";\n"


#

folder = "C:/Users/pc/OneDrive/Desktop/CV/"
for filename in os.listdir(folder):
    if os.path.isfile(folder + filename):
        if filename.endswith(".docx"):
            try:
                with open("resume.txt", "a") as r:
                    r.write(extractor(folder + filename))
            except AttributeError:
                continue
            except ValueError:
                continue
