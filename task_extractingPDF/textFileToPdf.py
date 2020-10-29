from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

file = open('git.text', 'r')
for data in file:
	pdf.cell(200,15, txt=str(data), ln=1, align='l')

pdf.output("mynewsample.pdf")