from authentication.library.authenticate import ServicePrincipal
from configparser import ConfigParser

config = ConfigParser()
config.read('configs/config.ini')

application_id = config.get('credentials', 'application_id')
application_secret = config.get('credentials', 'application_secret')
tenant_id = config.get('credentials', 'tenant_id')

client = ServicePrincipal(
    application_id= application_id,
    applicaton_secret= application_secret,
    tenant_id=tenant_id,
    scope=['https://analysis.windows.net/powerbi/api/.default'],
)

def save_token():
    client.save_token()

save_token()
