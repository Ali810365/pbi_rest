import json
from authentication.library.authenticate import User
from configparser import ConfigParser


config = ConfigParser()
config.read('configs/config.ini')

application_id = config.get('credentials', 'application_id')
application_secret = config.get('credentials', 'application_secret')

client = User(
    application_id= application_id,
    applicaton_secret= application_secret,
    scope=['https://analysis.windows.net/powerbi/api/.default'],
    redirect_uri= 'https://localhost/redirect'
)


    

def save_user_token():
    client.login()

def silent():
    with open('configs/credentials.json', 'r') as file:
        credentials = json.load(file)
    
    return client.silent_login(credentials['refresh_token'])