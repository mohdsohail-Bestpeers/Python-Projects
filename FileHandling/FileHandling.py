#reading 'abc.text' file using 'read' 
f=open('abc','r')
print(f.readline())
print(f.readline())


#Creating a text file using write:

f2= open('textFile','w')
f2.write("Created a text file using write")