# Module for extracting editable text
# The function must save the output to "./out/output.txt".

# Imports
import PyPDF2 # For parsing PDF documents

# The extraction function
def extract(filename):
	# Using the with-as syntax eliminates the need to close the file object manually and is safer
    with open(filename, 'rb') as book:
        # Initialize the PDF file object
        pdfReader = PyPDF2.PdfReader(book)
        pages = len(pdfReader.pages)
        print(f'Number of pages: {pages}')   
        text = []

        # Start reading the file from the first page
        # Note that the page numbers are 0-based i. e. Always 1 less than the desired value
        for num in range(pages):
            # Extract and pronounce the text for each page
            text.append(pdfReader.pages[num].extract_text())
            
        
        with open('./out/output.txt', 'w') as f:
                for line in text:
                	f.write(f'{line}')