import requests
import json
import pandas as pd
import csv

key = 'key=AIzaSyBqpUbJ-2sQ4LOEaOBTaotzZTo9SBWxWd4'
url_place_id_template_pt1 = 'https://maps.googleapis.com/maps/api/place/details/json?place_id='
url_place_id_template_pt2 = '&fields=name,formatted_phone_number,formatted_address,website&'



with open('./list.json', 'r') as file:
    contents:dict = json.load(file)



places_id_list = [item.get('place_id') for item in contents['results']]


place_id_details_list = []

for place_id in places_id_list:
    url = f'{url_place_id_template_pt1}{place_id}{url_place_id_template_pt2}{key}'

    response = requests.get(url)

    result = response.json()['result']

    place_id_details_list.append(result)


# with open('./places_details.txt', 'w+') as file:
#     file.write(str(place_id_details_list))


dt =  pd.DataFrame(data=place_id_details_list,columns=['name','formatted_phone_number','website','formatted_address'])

# with open ('./contacts.csv', 'w+', newline='') as csvfile:
#     csv.writer(dt, dialect='excel')

dt.to_csv('./tests/data.csv')
