# Module for extracting editable text
# The function must save the output to "./out/output.txt".

# Imports
import pyttsx3  # Speech synthesis
import PyPDF2  # For parsing PDF documents
from sys import stderr  # For displaying errors
from pathlib import Path  # For verifying the file

# TODO
# The extraction function


def extract(filename):
    with open(book_file, 'a') as book:
	pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
	print(f'Initializing the parser object')
		
    with open(book_file, 'a') as book:
	dirs = os.path.join(os.getcwd(), 'out', 'output.txt')
	print(f'Writing the content to a new file')
	for num in range(page_number - 1, pages):
        text = pdfReader.getPage(num).extractText()
        print(text, file=book)          
