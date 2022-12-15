#import necessary libraries
import requests
import json
import pandas as pd
from pathlib import Path

#obtain url property from config.json file
with open('/data/config.json') as f:
    json_data = json.load(f)
    url = json_data['parameters']['url']
    path = json_data['parameters']['path']
    name = json_data['parameters']['name']
    
#request url and save response into variable
r = requests.get(url)

#create full path for the file, make parent directory
full_path = '/data/out/tables/' + path + "/" + name
Path('/data/out/tables/' + path).mkdir(parents=True, exist_ok=True)

#create or open (if exists) output file for writing and write the content of the response
with open(full_path, 'wb') as f:
    f.write(r.content)

#read output file and print to console log first 10 rows
data = pd.read_csv(full_path, header=0)
print(data.loc[0:10,["Name", "Survived"]])
