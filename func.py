import requests
import sys


class Mapping:

    def __init__(self):
        self.search_api_server = "https://search-maps.yandex.ru/v1/"
        self.map_request = "http://static-maps.yandex.ru/1.x/?bbox={0}~{1}&l={2}&size=600,450"
        self.api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
        self.location = [36.593419, 55.117073]
        self.l_map = 'map'
        self.spn = 0.01
        # 55.117073, 36.593419

    def start(self):
        left = [str(self.location[0]-self.spn), str(self.location[1]-self.spn)]
        right = [str(round(self.location[0]+self.spn, 6)), str(round(self.location[1]+self.spn, 6))]
        map_request_now = self.map_request.format(','.join(left), ','.join(right), self.l_map)
        response1 = requests.get(map_request_now)
        map_file1 = "map1.png"
        try:
            with open(map_file1, "wb") as file:
                file.write(response1.content)
        except IOError as ex:
            print("Ошибка записи временного файла:", ex)
            sys.exit(2)
        return map_file1


