from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200,10,txt="Hello this is python file ",ln=1,align='C')
pdf.cell(200,10,txt="converted into pdf....!!!",ln=2, align="C")

pdf.output('MyTexrTOPdf.pdf')