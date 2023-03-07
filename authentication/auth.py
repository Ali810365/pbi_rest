import msal
import json
import time
from configparser import ConfigParser

config = ConfigParser()
config.read('configs/config.ini')

application_id = config.get('credentials', 'application_id')
application_secret = config.get('credentials', 'application_secret')
tenant_id = config.get('credentials', 'tenant_id')

scope = ['https://analysis.windows.net/powerbi/api/.default']
AUTHORITY_URL = 'https://login.microsoftonline.com/{}'.format(tenant_id)
        
client = msal.ConfidentialClientApplication(
            client_id= application_id,
            client_credential= application_secret,
            authority=AUTHORITY_URL
        )


def grab_access_token():
    token = client.acquire_token_for_client(
    scopes=scope
    )

    return token

def save_token(): #saving the token to file
    response = grab_access_token()
    credentials = {}
    credentials['auth_type'] = 'service_principal' 
    credentials['token_type'] = response['token_type'] 
    credentials['expire_in'] = time.time() + response['expires_in'] 
    credentials['ext_expires_in'] = time.time() + response['ext_expires_in']
    credentials['access_token'] = response['access_token']

    with open('configs/credentials.json', 'w') as f:
        f.write(json.dumps(credentials, indent=2))

















