# Email-Extractor
This extractor works on both Microsoft Word Documents and PDF files.
It iterates through all the files in a folder, picks the files that are .PDF or .Docx, 
searches through for email addresses, then returns the first email address with a semicolon on a new line.
If an email match isn't found, it adds a blank new line with a semicolon.
