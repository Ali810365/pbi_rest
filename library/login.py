import json
import time
import pathlib
from authentication.service_principal import save_token

does_exist = pathlib.Path('configs/credentials.json').exists()

def fetch_token():
    if does_exist:
        with open('configs/credentials.json', 'r') as file:
            data = json.load(file)
        #determine if token has expired or not
        expires_in = data['expires_in'] - time.time()
        if expires_in < 100:
            return 0
        else:
            return expires_in
    else:
        return 0

def login():
    if fetch_token() > 100:
        with open('configs/credentials.json', 'r') as file:
            data = json.load(file)
        return data['access_token']
    else:
        save_token()
        with open('configs/credentials.json', 'r') as file:
            data = json.load(file)
        return data['access_token']


access_token = login()

headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }



