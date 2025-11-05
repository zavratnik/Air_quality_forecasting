import json
import requests
import pandas as pd
import numpy as np
import pprint

url = "https://arsoxmlwrapper.app.grega.xyz/api/air/archive"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    with open('data/raw/air/neobdelani_podatki.json', 'w') as f:
        json.dump(data, f)
else:
    print(f"Error: {response.status_code}")