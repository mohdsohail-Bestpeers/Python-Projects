import PyPDF2

a=PyPDF2.PdfFileReader('python_tutorial_book.pdf')
print(a.documentInfo)
