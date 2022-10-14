# Module for extracting editable text
# The function must save the output to "./out/output.txt".

# Imports
# TODO

# The extraction function 
#extract the files from input dictionary and save them to output dictionary


def extract(filename):
	# TODO
	# Open the file
	# Extract text
	# Save text to file
	# Close the file
	# Open the file
	with open(filename, 'rb') as f:
		# Extract text
		pdfReader = PyPDF2.PdfFileReader(f)
		num_pages = pdfReader.numPages
		count = 0
		text = ""
		#The while loop will read each page
		while count < num_pages:
			pageObj = pdfReader.getPage(count)
			count +=1
			text += pageObj.extractText()
		# Save text to file
		with open('out/output.txt', 'w') as f:
			f.write(text)
		# Close the file
		f.close()


	