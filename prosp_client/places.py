from pathlib import Path
import json
import urllib.request
import pandas as pd
from os import environ
from time import sleep


# Essa classe faz request para o link prencipal e salva o resultado em um arquivo .json
class RequestPlaces:

    def __init__(self, url):
        self.__url =  url
        self.result = self.request(self.__url)
        self.json_obj = self.deserialize_json_and_get_content(self.result)
        self.json_obj_list = []
        self.json_obj_list.append(self.json_obj)

        for index in range(1, 4):
            if 'next_page_token' in self.json_obj:
                self.base_link = 'https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken='
                self.pagetoken = self.json_obj['next_page_token']
                self.key_link_part = '&key='
                self.__key = environ['GMAP_KEY']
                self.__page_token_url = self.join_link()
                sleep(2)
                self.result = self.request(self.__page_token_url)
                self.json_obj = self.deserialize_json_and_get_content(self.result)
                self.json_obj_list.append(self.json_obj)

    
    def request(self, url):
        print(url)
        result = urllib.request.urlopen(url)
        return result


    def deserialize_json_and_get_content(self, result):
        content = json.load(result)
        
        if content["status"] in ["OK", "ZERO_RESULTS"]:
            return content
        else:
            raise Exception(content["error_message"])


    def join_link(self):
        link = self.base_link + self.pagetoken + self.key_link_part + self.__key        
        return link

    
    def __str__(self):
        return self.join_link()


    def writing_json_file(self):
        # encoding em utf-8 e setando ascii para false(obeter caracteres com acento)
        with open('./prosp_client/json/teste2.json', 'w+', encoding='utf-8') as file:
            json.dump(self.json_obj_list, file, indent=2, ensure_ascii=False)


# Essa clase abre o arquivo .json e faz o parse dos place_id em uma lista
class PlaceIdsList:

    def __init__(self):
        self.content = self.open_and_deserialize_json_file()
        self.__id_list = self.get_place_ids(self.content)

    
    def open_and_deserialize_json_file(self):
        with open('./prosp_client/json/teste2.json', 'r') as file:
            content:dict = json.load(file)

        return content

    
    def get_place_ids(self, content):
        places_id_list = list()
        
        for page in content:
            ids_list = [item.get('place_id') for item in page['results']]
            places_id_list.append(ids_list)

        return places_id_list


    @property
    def id_list(self):
        return self.__id_list


class  ContentToCsv:

    def __init__(self, urls):
        self.__urls = urls
        self.__cotent_list = self.deserialize_json_and_get_content(self.__urls)


    def request(self, url):
        result = urllib.request.urlopen(url)
        return result


    def deserialize_json_and_get_content(self, urls):
        content_list = list()

        for url in urls:
            result = self.request(url)

            content = json.load(result)

            if content["status"] in ["OK", "ZERO_RESULTS"]:
                content_list.append(content['result'])
            else:
                raise Exception(content['error_message'])


        return content_list


    @property
    def content_list(self):
        return self.__cotent_list


    def save_csv_file(self):
        data_frame = pd.DataFrame(data=self.__cotent_list, columns=['name','formatted_phone_number','website','formatted_address'])
        data_frame.to_csv('./prosp_client/csv/data.csv')