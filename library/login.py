import json
import time
import pathlib
from authentication.service_principal import save_token
from authentication.user import save_user_token, silent


does_exist = pathlib.Path('configs/credentials.json').exists()


def fetch_token():
    if does_exist:
        with open('configs/credentials.json', 'r') as file:
            credentialsFile = json.load(file)
        #determine if token has expired or not
        expires_in = credentialsFile['expires_in'] - time.time()
        if expires_in < 100:
            return 0
        else:
            return expires_in
    else:
        return "No Credentials"

def authenticated():
    if fetch_token() == "No Credentials":
        return False
    else:
        return True


def login():
    if authenticated():
        if fetch_token() > 100:
            with open('configs/credentials.json', 'r') as file:
                credentialsFile = json.load(file)
            return credentialsFile['access_token']
        else:
            with open('configs/credentials.json', 'r') as file:
                credentialsFile = json.load(file)
            
            if credentialsFile['auth_type'] == 'service_principal':
                save_token()
                with open('configs/credentials.json', 'r') as file:
                    credentialsFile = json.load(file)
                return credentialsFile['access_token']
            elif credentialsFile['auth_type'] == 'user':
                #try to silent login in first
                refresh_token = silent()
                
                if 'error' in refresh_token:
                    save_user_token()
                    with open('configs/credentials.json', 'r') as file:
                        credentialsFile = json.load(file)
                    return credentialsFile['access_token']
                else:
                    with open('configs/credentials.json', 'r') as file:
                        credentialsFile = json.load(file)
                    return credentialsFile['access_token']

    else:
        return 'invalid'

with open('configs/credentials.json', 'r') as file:
    credentialsFile = json.load(file)
    
access_token = login()

headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }



