import pprint
import requests
import json

class Client(object):

    def __init__(self) -> None:
        self.url1 = "http://api.ipify.org/?format=json"
        self.url2 = "https://ipinfo.io/"
        self.url2suf = ""

    def get_api(self, url):
        result = requests.get(url)
        dades = json.loads(result.text)
        return dades

    def get_myip(self):
        dades = self.get_api(self.url1)
        return dades["ip"]

    def get_indo(self, ip):
        dades = self.get_api(self.url2+ip+self.url2suf)
        return dades

    def select_data(self, data):
        dades = []
        for e in data['feed']['entry']:
            title = e['title']
            dades.append(title)
        return dades
        # dades = [e['title'] for e in data['feed']['entry']]

    def get_data(self):
        # descarregar-se dades
        myip = self.get_myip()
        # llegir xml
        dades = self.get_info(myip)
        # retornar dades
        dades = self.parse_json(dades)
        return dades

if __name__ =="__main__":
    client = Client()
    dades = client.get_data()
    pprint.print(dades)

