import PyPDF2

a=PyPDF2.PdfFileReader('python_tutorial_book.pdf')
#counting the page of the book
print(a.getNumPages())
