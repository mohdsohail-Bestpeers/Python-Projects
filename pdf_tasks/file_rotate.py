# Rotating pdf
import PyPDF2

pdf_reader = PyPDF2.PdfFileReader('python_tutorial_book.pdf')
pdf_writer = PyPDF2.PdfFileWriter()


#rotating first page of book 
page = pdf_reader.getPage(2)
page.rotateClockwise(90)

pdf_writer.addPage(page)
resultFile = open('new_python_tutorial_book.pdf.pdf', 'wb')
pdf_writer.write(resultFile)
resultFile.close()


'''
import fitz

pdf =fitz.open('python_tutorial_book.pdf')
#numPages=pdf.pageCount()

pdf2 = fitz.open()
pdf2.insertPDF(pdf, from_page=0, to_page=numPage-1, rotate=90)
pdf2.save('output.pdf')'''