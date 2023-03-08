import json
import requests
from library.admin import Admin

dummy = "3b5ca243-47d1-4be5-ac56-57c62291607d"

id = "2b5ca223-46d1-4be5-ac56-57c62291607d" #test
dashboard = "0b0f429f-ed67-4a0b-bdd6-1c358d702db7"
user = "aabdi@redapt.com"
admin = Admin()

print(admin.get_activity_events("2023-03-06T00:00:00.000Z", "2023-03-06T20:59:00.000Z"))