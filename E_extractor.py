"""
import os
import re

path = "C:/Users/pc/Downloads/Compressed/HI_candidates/NitarandaAlexander__CV.docx"
print(os.listdir(path))


def pathOpener(filePath):
    for x in os.listdir(filePath):
        try:
            opener = open(filePath + x)
        except PermissionError:
            continue
        print(opener)
        return opener


pathOpener(path)


with open("C:/Users/pc/Downloads/Compressed/HI_candidates/NitarandaAlexander__CV.docx") as file:
    for email in file:
        str.encode(email)
        print(email.split('@'))
"""
import re
import docx
import os


def extractor(folder_path):
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
    return ans+";\n"


# extractor("C:/Users/pc/OneDrive/Desktop/CV/Assumpta Akuoma Onuoha.docx")

folder = "C:/Users/pc/OneDrive/Desktop/CV/"
for filename in os.listdir(folder):
    if os.path.isfile(folder + filename):
        if filename.endswith(".docx"):
            try:
                with open("resume.txt", "a")  as r:
                    r.write(extractor(folder + filename))
            except AttributeError:
                continue
            except ValueError:
                continue
