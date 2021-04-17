from files_and_requests import TextSearch, PlaceIdsDetailsList
from places import RequestPlaces, PlaceIdsList, ContentToCsv
from pathlib import Path
import json
import urllib.request

while True:
    to_search = str(input('Digite: '))
    advg = TextSearch(to_search)
    print(advg)
    # # print(id(advg))
    # resp = RequestPlaces(advg.url)
    # resp.writing_json_file()

    # ids = PlaceIdsList()
    # list_ids = PlaceIdsDetailsList(ids.id_list)
    # csv = ContentToCsv(list_ids.urls)
    # print(csv.content_list)
    # csv.save_csv_file()
# print(advg)
# print(advg.url)


# p = Path('./prosp_client')

# print([x for x in p.iterdir() if x.is_dir()])

# print(list(p.glob('*.csv')))


