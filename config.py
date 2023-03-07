from configparser import ConfigParser
import pathlib

# Create configs folder if it does not exist
path = pathlib.Path('configs')
path.mkdir(parents=True, exist_ok=True)


# Initialize the config Parser.
config = ConfigParser()

#add a section in the config file
config.add_section('credentials')
config.set('credentials', 'application_id', '') #application id goes in between the quotes
config.set('credentials', 'application_secret', '') #application secret goes in between the quotes
config.set('credentials', 'tenant_id', '') #tenant id goes in between the quotes

config.add_section('username')
config.set('username', 'application_id', '') #application id goes in between the quotes
config.set('username', 'user_name', '') #application secret goes in between the quotes
config.set('username', 'password', '') #tenant id goes in between the quotes


# Write to a config.ini file.
with open(file='configs/config.ini', mode='w+') as f:
    config.write(f)