from os import environ
import urllib.request



# Essa classe recebe o paramentro para pesquisa e forma o link principal
class TextSearch:
    
    def __init__(self, places_to_search):
        self.base_link = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='
        self.__places_to_search =  self.formart_search_link_part(places_to_search)
        self.key_link_part = '&key='
        self.__key = environ['GMAP_KEY']
        self.__url = self.join_link()


    def join_link(self):
        link = self.base_link + self.__places_to_search + self.key_link_part + self.__key        
        return link

    
    def __str__(self):
        return self.join_link()


    def formart_search_link_part(self, link_part):
        splited_link_part = link_part.split()
        link_part_formatted = '+'.join(splited_link_part)

        return link_part_formatted
    
    
    @property
    def url(self):
        return self.__url


# Essa classe faz o join dos id_place e forma os links
class PlaceIdsDetailsList:

    def __init__(self,place_ids_list):
        self.__place_ids_list = place_ids_list
        self.base_link = 'https://maps.googleapis.com/maps/api/place/details/json?place_id='
        self.params = '&fields=name,formatted_phone_number,formatted_address,website'
        self.key_link_part = '&key='
        self.__key = environ['GMAP_KEY']
        self.__urls = self.join_links_list()



    def join_links_list(self):

        url_place_ids_list = list()

        for url in self.__place_ids_list:
            url_place_id = self.base_link + url + self.params + self.key_link_part + self.__key        
            url_place_ids_list.append(url_place_id)

        return url_place_ids_list


    @property
    def urls(self):
        return self.__urls