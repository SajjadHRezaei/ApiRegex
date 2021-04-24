import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/asia"

headers = {
    'x-rapidapi-key': "a4fa9fadb3msh2dbc8b75d752a88p1b12aajsn790cda69ac1a",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

import json
res_dict=json.loads(response.text)
res_dict

df=pd.DataFrame(res_dict)
fig, axs = plt.subplots(ncols=1, nrows=6, figsize=(20, 60))
cols=['rank','Infection_Risk','Test_Percentage','Recovery_Proporation','Deaths_1M_pop','Tests_1M_Pop']

for i,k in enumerate (cols):
    sns.barplot(data=df,y='Country',x=k,ax=axs[i] , palette = 'hls',ci='sd',capsize = 0.3 ,saturation=0.8)
    #plt.xticks(rotation=45)
