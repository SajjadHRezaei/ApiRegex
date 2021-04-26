import requests
import json
import pandas as pd
url = "https://weatherapi-com.p.rapidapi.com/current.json"

city_list=['London', 'Paris', 'Tehran', 'Berlin', 'Tokyo']

data={}   
for city_name in city_list:
    querystring = {"q":city_name}

    headers = {
        'x-rapidapi-key': "a4fa9fadb3msh2dbc8b75d752a88p1b12aajsn790cda69ac1a",
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data[city_name]=json.loads(response.text)

data
#%%
df=pd.DataFrame.from_dict({(i,j): data[i][j] 
                           for i in data.keys() 
                           for j in data[i].keys()},
                       orient='columns').T
df=df.drop(index='location',level=1)
df=df.drop(['name','region','country','lat','lon','tz_id','localtime_epoch','localtime','condition'],axis=1)
df.reset_index(inplace=True)
df.drop(['level_1'],axis=1,inplace=True)
df.rename(columns={"level_0": "city"},inplace=True)
df.T
#%%
import matplotlib.pyplot as plt
import seaborn as sns


fig, axs = plt.subplots(ncols=1, nrows=6, figsize=(20, 60))
cols=['temp_c','wind_kph','pressure_in','cloud','feelslike_c','uv']

for i,k in enumerate (cols):
    sns.barplot(data=df,x='Country',y=k,ax=axs[i] , palette = 'hls',ci='sd',capsize = 0.3 ,saturation=0.8)
    #plt.xticks(rotation=45)
#%%
