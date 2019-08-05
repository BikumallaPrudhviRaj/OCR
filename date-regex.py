# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:53:04 2019

@author: Prudhvi.Bikumalla
"""

import re
import datetime
filepath = r'C:\Users\Prudhvi\Desktop\petchem\invoice_data\New Text Document.txt'
datepattern = '%d.%m.%Y'
with open(filepath, 'r') as f:
	file = f.read()
x = re.findall('\d\d.\d\d.\d\d\d\d', file)
z = re.findall(r'Ca\w+ \Desc\w+',file)
print(z)
y = []
for item in x:
	try:
		date = datetime.datetime.strptime(item, datepattern)
		y.append(date)
	except:
		pass
res = []
for item in y:
	a, b = str(item).split('')
	res.append(a)
	
for item in res: print(item)

print(z)