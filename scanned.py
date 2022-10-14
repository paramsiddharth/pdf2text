# Module for extracting scanned text
# The function must save the output to "./out/output.txt".
# The images must temporarily be stored in "./out/imgs/", and deleted after being processed.

# Imports
import pytesseract  

# The extraction function
def extract(filename):
	# TODO
	# Open the file
	# Extract text
	# Save text to file
	# Close the file
	# Open the file
	with open(filename, 'rb') as f:
		# Extract text
		pdfReader=pytesseract.image_to_string(f)
		# Save text to file
		with open('out/output.txt', 'w') as f:
			f.write(pdfReader)
		# Close the file
		f.close()
