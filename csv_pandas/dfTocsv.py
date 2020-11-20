'''convert dataframe to csv'''
import numpy as np
import pandas as pd

dict={
    "name":['vijay','faiz','aadil','raise'],
    "rollNo":['100','102','103','104'],
    "city":['indore','mumbai','delhi','ratlam']
}

df=pd.DataFrame(dict)
'''TO CHECK DICT'''
print(df)

'''CONVERT DF TO CSV'''
#df.to_csv('converted.csv')


'''REMOVE ID FROM CSV'''
#df.to_csv('removeID.csv',index=False)



'''TO CHECK FIRST ROW USE #head'''
#df.head(2)        # IT SHOW 0 TO 1 ROWS
#print(df)



'''TO CHECK FIRST ROW USE #tail'''
#df.tail(2)        # IT SHOW 3 TO 4 ROWS
#print(df)
