import re
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
data = requests.get(url)
if str(data)=='<Response [200]>':
    print("The web page is loaded successfully")
#load data into soup variable
soup = BeautifulSoup(data.text, 'html.parser')

#find table and table data
table_1 = soup.find('table', {'class':"wikitable sortable",'id':"constituents"})
tablebody = table_1.find('tbody')
ssp=[]
for i,row in enumerate(tablebody.find_all('tr')):
    if i==0:
        th = row.find_all('th')
        title = [i.text.strip() for i in th]
    else:
        td = row.find_all('td')
        table_row = [i.text.strip() for i in td]
        ssp.append(table_row)
ssp=ssp[::-1]

df = pd.DataFrame.from_records(ssp)
df.columns=title
df

##
#second table
table_2 = soup.find('table', {'class':"wikitable sortable",'id':'changes'})
tablebody = table_2.find('tbody')


ssp2=[]
for i,row in enumerate(tablebody.find_all('tr')):
    if i>1:
        td = row.find_all('td')
        table_row = [re.split('.\d+.\n', i.text)[0] for i in td]
        ssp2.append(table_row)
ssp2=ssp2[::-1]

##
df2 = pd.DataFrame.from_records(ssp2)
df2.columns = ['Date', 'Added Ticker', 'Added Security','Removed Ticker ', 'Removed Security', 'Reason']
df2