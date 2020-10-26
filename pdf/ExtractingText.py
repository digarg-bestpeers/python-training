import PyPDF2
pdfFileObj = open('git.pdf', 'rb')		# creating a pdf file object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)	# creating a pdf reader object 
print(pdfReader.numPages)		# printing number of pages in pdf file 

pageObj = pdfReader.getPage(0)			# creating a page object
print(pageObj.extractText())			# extracting text from page
pdfFileObj.close()