import numpy as np
import pandas as pd

dict={
    "name":['vijay','faiz','aadil','raise'],
    "rollNo":['100','102','103','104'],
    "city":['indore','mumbai','delhi','ratlam']
}

df=pd.DataFrame(dict)
#print(df)


'''CHANGING INDEX O,1,2 TO NAMES'''
file1=pd.read_csv('indexname.csv')
file1.index=['A','B','C','D']
print(file1) 


