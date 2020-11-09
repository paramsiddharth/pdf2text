# Module for extracting editable text
# The function must save the output to "./out/output.txt".

# Imports
import pyttsx3 # Speech synthesis
import PyPDF2 # For parsing PDF documents
from sys import stderr # For displaying errors
from pathlib import Path # For verifying the file

# TODO
# The extraction function
def extract(filename):
	book_file = input('Enter the name of the file: ')
	# Creating output folders 
	dirs = os.path.join(os.getcwd(), 'out', 'output.txt')
	if not Path(dirs).is_dir():
		os.makedirs(dirs)
	if Path(f'./{book_file}').is_file():
	    # Using the with-as syntax eliminates the need to close the file object manually and is safer
	    with open(book_file, 'a') as book:
		# Initialize the PDF file object
		pdfReader = PyPDF2.PdfFileReader(book)
		pages = pdfReader.numPages

		# Set page_number to the first page in the case of invalid input
		if page_number > pages:
		    print(f'Error: {page_number} exceeds the number of available pages.', file=stderr)
		    page_number = 1

		for num in range(page_number - 1, pages):
		    # Extract and pronounce the text for each page
		    text = pdfReader.getPage(num).extractText()
		    print(text)

	else:
	    print('Error: File inaccessible!', file=stderr) # Couldn't read the file
