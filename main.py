# Main application with console-based user interaction

# Imports
from sys import exit, stderr # For error-handling
from pathlib import Path # To check for files and folders
import os # For directory operations

def main():
	# Imports
	from editable import extract as extract_editable # Extract editable_text
	from scanned import extract as extract_scanned # Extract scanned text

	# Create output folders if they don't exist
	dirs = os.path.join(os.getcwd(), 'out', 'imgs')
	if not Path(dirs).is_dir():
		os.makedirs(dirs)

	# Introduction
	print('''\
	------------------------------------
	The Ultimate PDF to Text Converter
	------------------------------------

	\
	''')

	# Read the input

	# File
	file_name = None
	while True:
		file_name = input('Locate the file: ')
		if Path(file_name).is_file():
			break
		print('Invalid file!', file=stderr)
	if file_name is None:
		print('Invalid input!', file=stderr)
		exit(1)

	# Method of extraction
	print('''\

	What kind of text does the PDF file contain?
	1. Editable
	2. Scanned
	\
	''')
	choice = None
	while True:
		choice = input('Enter your choice: ')
		if choice.strip() in ('1', '2'):
			break
		print('Invalid choice!', file=stderr)
	if choice is None:
		print('Invalid input!', file=stderr)
		exit(1)

	# Begin execution
	if choice == '1':
		# Use simple text extraction
		extract_editable(file_name)
	else:
		# Use OCR to parse text
		extract_scanned(file_name)

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(str(e), file=stderr)