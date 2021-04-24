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