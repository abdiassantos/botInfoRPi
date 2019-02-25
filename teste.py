import re
import json
from urllib.request import urlopen
import requests
import urllib

url = 'http://ipinfo.io/json'
#response = urlopen(url)
#data = json.load(response)
data = requests.get(url).json()

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

print('Your IP detail\n ')
print('IP : {}'.format(IP))

