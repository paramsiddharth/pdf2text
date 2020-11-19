# Module for extracting editable text
# The function must save the output to "./out/output.txt".

# Imports
import pyttsx3  # Speech synthesis
import PyPDF2  # For parsing PDF documents
from sys import stderr  # For displaying errors
from pathlib import Path  # For verifying the file
import os # For directory operations

def extract(filename):
    with open(filename, 'a') as book:
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
    print(f'Initializing the parser object')

    with open(filename, 'a') as book:
        dirs = os.path.join(os.getcwd(), 'out', 'output.txt')
        print(f'Writing the content to a new file')
        for num in range(pages):
            text = pdfReader.getPage(num).extractText()
            print(text, file=book)
