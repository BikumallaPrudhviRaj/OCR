# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:52:35 2019

@author: Uday.Menon
"""
import camelot
import pandas as pd
import re

#250616004

tables_1_a = camelot.read_pdf(r'C:\Users\udaym\Desktop\CP-ML\Petchem\250616004\250616004A.pdf')

tables_1_a[0] #Table Shape

tables_1_a[0].parsing_report

doc1_tabdfA = tables_1_a[0].df

tables_1_b = camelot.read_pdf(r'C:\Users\udaym\Desktop\CP-ML\Petchem\250616004\250616004B.pdf')

tables_1_b[0] #Table Shape

tables_1_b[0].parsing_report

doc1_tabdfB = tables_1_b[0].df

tables_1_c = camelot.read_pdf(r'C:\Users\udaym\Desktop\CP-ML\phototest.pdf',flavor='stream',row_tol=10)

tables_1_c[0] #Table Shape

tables_1_c[0].parsing_report
camelot.plot(tables_1_c[0], kind='grid')

doc1_tabdfC = tables_1_c[0].df

#250598825

tables_2_a = camelot.read_pdf(r'C:\Users\Prudhvi\Desktop\petchem\invoice_data\page_docC250_1ser.pdf')

tables_2_a[0] #Table Shape
tables_2_a[1]
tables_2_a[1].parsing_report
camelot.plot(tables_2_a[0], kind='grid')
doc2_tabdfA = tables_2_a[1].df
#doc2_tabdfA_new = pd.Series('doc2_tabdfA')
doc2_tabdfA_new = []
doc2_tabdfA_new1 = []

#for i in range(len(doc2_tabdfA.index)):
 #   doc2_tabdfA_new.append(doc2_tabdfA.iloc[i])
for i in range(len(doc2_tabdfA.columns)):
     doc2_tabdfA_new.append(doc2_tabdfA[i].astype(str))

for columns in (doc2_tabdfA_new):
    for row in columns:
        doc2_tabdfA_new1.append(row)
    
for q in range(len(doc2_tabdfA_new1)):
    if(re.findall('\Desc\w+ of \w+',doc2_tabdfA_new1[q])):
        print(q)
        print(doc2_tabdfA_new1[q+1])


doc2_tabdfA_new1=  doc2_tabdfA[0].astype(str)

tables_2_b = camelot.read_pdf(r'C:\Users\Prudhvi\Desktop\petchem\invoice_data\250611854  B.pdf')

tables_2_b[1] #Table Shape

tables_2_b[1].parsing_report

doc2_tabdfB = tables_2_b[1].df

doc2_tabdfB_new = []
doc2_tabdfB_new1 = []


for i in range(len(doc2_tabdfB.columns)):
     doc2_tabdfB_new.append(doc2_tabdfB[i].astype(str))

for columns in (doc2_tabdfB_new):
    for row in columns:
        doc2_tabdfB_new1.append(row)
    
for q in range(len(doc2_tabdfB_new1)):
    if(re.findall(r'\Desc\w+ of \w+|Ca\w+ \Desc\w+',doc2_tabdfB_new1[q])):
        print(q)
        print(doc2_tabdfB_new1[q+1])

tables_2_c = camelot.read_pdf(r'C:\Users\udaym\Desktop\CP-ML\Petchem\250598825\250598825\250598825 C.pdf')

tables_2_c[0] #Table Shape

tables_2_c[0].parsing_report

doc2_tabdfC = tables_2_c[0].df
#####################################

#250609529

tables_3_a = camelot.read_pdf(r'C:\Users\udaym\Desktop\CP-ML\Petchem\250609529\250609529\250609529 A.pdf')

tables_3_a[0] #Table Shape

tables_3_a[0].parsing_report

doc3_tabdfA = tables_3_a[0].df

tables_3_b = camelot.read_pdf(r'C:\Users\udaym\Desktop\CP-ML\Petchem\250609529\250609529\250609529 B.pdf')

tables_3_b[0] #Table Shape

tables_3_b[0].parsing_report

doc3_tabdfB = tables_3_b[0].df

tables_3_c = camelot.read_pdf(r'C:\Users\udaym\Desktop\CP-ML\Petchem\250609529\250609529\page_docC_1_sandwich.pdf',flavor='stream')

tables_3_c[0] #Table Shape

tables_3_c[0].parsing_report
camelot.plot(tables_3_c[0], kind='grid')
camelot.plot(tables_3_c[0], kind='contour')
camelot.plot(tables_3_c[0], kind='line')

doc3_tabdfC = tables_3_c[0].df

#####################################

#250611854

tables_4_a = camelot.read_pdf(r'C:\Users\udaym\Desktop\CP-ML\Petchem\250611854\250611854\250611854 A.pdf')

tables_4_a[0] #Table Shape

tables_4_a[0].parsing_report

doc4_tabdfA = tables_4_a[0].df

tables_4_b = camelot.read_pdf(r'C:\Users\udaym\Desktop\CP-ML\Petchem\250611854\250611854\250611854 B.pdf')

tables_4_b[0] #Table Shape

tables_4_b[0].parsing_report

doc4_tabdfB = tables_4_b[0].df

tables_4_c = camelot.read_pdf(r'C:\Users\udaym\Desktop\CP-ML\Petchem\250611854\250611854\250611854 C.pdf')

tables_4_c[0] #Table Shape

tables_4_c[0].parsing_report

doc4_tabdfC = tables_3_c[0].df
