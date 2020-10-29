from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200,10,txt="Welcome in python",ln=1,align='C')
pdf.cell(200,10,txt="Hi, how are you", ln=2,align="C")

pdf.output('mysample.pdf')


