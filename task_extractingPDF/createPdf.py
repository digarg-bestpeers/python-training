# Creating pdf from existing pdf

from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_writer = PdfFileWriter()
pdf_reader = PdfFileReader('sample.pdf')

for page in range(pdf_reader.numPages):
	obj = pdf_reader.getPage(page)
	pdf_writer.addPage(obj)

output_file = open('output.pdf', 'wb')
pdf_writer.write(output_file)
print('File created successfully')
