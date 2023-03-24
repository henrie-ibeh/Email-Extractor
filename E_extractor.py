# import re for regular expression usage, os for the ability to iterate through a folder, PyPDF2 for PDF manipulation
# docx for MS Word manipulation (the module for docx is actually 'python-docx' but is imported as 'docx')
import re
import os
from PyPDF2 import PdfReader
from docx import Document


def extractor(folder_path):
    # extracts document contents
    def readtextdoc(path):
        # creates a document object
        doc = Document(path)

        # creates an empty list for document paragraphs to be stored
        completedText = []

        # iterates through the documents, extracts each paragraph and stores it completedText variable list
        for paragraph in doc.paragraphs:
            completedText.append(paragraph.text)

        # joins all the paragraphs into one text line
        return "\n".join(completedText)

    text = readtextdoc(folder_path)
    # creates email regex pattern
    pattern = re.compile(r'[a-zA-Z\d_.+-]+@[a-zA-Z\d-]+\.[a-zA-Z\d.-]+')

    # searches for matches within the text file
    matches = pattern.finditer(text)

    # function that picks the first match of the email (because usually the personal email comes first)
    def first_match(match):
        ma = 1
        for i in match:
            if ma < 2:
                print(i.group(0))
                ma += 1
                return i

    # converts the object to string
    ans = str(first_match(matches).group(0))
    # adds semicolon and new line after each text
    return ans + ";\n"


def readtextpdf(path):
    # creates object from pdf file
    reader = PdfReader(path)

    # collects the page number
    page = reader.pages[0]

    # extracts texts from pages
    text = page.extract_text()
    # email regex pattern
    pattern = re.compile(r'[a-zA-Z\d_.+-]+@[a-zA-Z\d-]+\.[a-zA-Z\d.-]+')

    # searches for matches within the text file
    matches = pattern.finditer(text)

    # function that picks the first match of the email (because usually the personal email comes first)
    def first_match(match):
        ma = 1
        for i in match:
            if ma < 2:
                print(i.group(0))
                ma += 1
                return i

    # converts the object to string
    ans = str(first_match(matches).group(0))
    # adds semicolon and new line after each text
    return ans + ";\n"


# folder path where documents and pdf are stored
folder = "C:/Users/ibehh/Documents/PycharmProjects/E_extractorProject/Upload CV/"

# iterating through files in the folder, matching emails from each and saving them in 'resume.txt' file
for filename in os.listdir(folder):
    if os.path.isfile(folder + filename):
        # checking if the file is a pdf file, append email to txt file with new line else add new line and continue
        if filename.endswith(".pdf"):
            try:
                with open("resume.txt", "a") as r:
                    r.write(readtextpdf(folder + filename))
            # errors simply add new lines and prints file names
            except AttributeError:
                with open("resume.txt", "a") as r:
                    r.write(';\n')
                print(filename)
                continue
            except ValueError:
                with open("resume.txt", "a") as r:
                    r.write(';\n')
                print(filename)
                continue
        # checking if the file is an MS Word file, append email to txt file with new line else add new line and continue
        elif filename.endswith(".docx"):
            try:
                with open("resume.txt", "a") as r:
                    r.write(extractor(folder + filename))
            # errors simply add new lines and prints file names
            except AttributeError:
                with open("resume.txt", "a") as r:
                    r.write(';\n')
                print(filename)
                continue
            except ValueError:
                with open("resume.txt", "a") as r:
                    r.write(';\n')
                print(filename)
                continue
