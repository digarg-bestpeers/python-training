# Rotating pdf
import PyPDF2

pdf_reader = PyPDF2.PdfFileReader('sample.pdf')
pdf_writer = PyPDF2.PdfFileWriter()

page = pdf_reader.getPage(1)
page.rotateClockwise(90)

pdf_writer.addPage(page)
resultFile = open('new_sample.pdf', 'wb')
pdf_writer.write(resultFile)
resultFile.close()