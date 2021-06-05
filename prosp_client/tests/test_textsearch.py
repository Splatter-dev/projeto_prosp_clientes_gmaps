import requests
import json
from os import environ

key = 'AIzaSyBqpUbJ-2sQ4LOEaOBTaotzZTo9SBWxWd4'
url_text_search = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='


json_result = requests.get(f'{url_text_search}+"advogados+em+indaiatuba"+&key={key}').text


with open('./tests/list.json', 'w+') as file:
    file.write(json_result)

print(environ['GMAP_KEY'])
