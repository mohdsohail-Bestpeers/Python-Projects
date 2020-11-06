import PyPDF2

a=PyPDF2.PdfFileReader('python_tutorial_book.pdf')
str=""
for i in range(1,11):
    str +=a.getPage(i).extractText()

#create a text file in which the data will store
with open("text.txt","w") as f:
    f.write(str)