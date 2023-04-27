from authentication.library.authenticate import User
from configparser import ConfigParser
import json

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

client.login()

with open('configs/credentials.json', 'r') as file:
    data = json.load(file)

print(client.silent_login(data['refresh_token']))