import urllib3
import bs4

class Client(object):

    def __init__(self) -> None:
        self.url = "https://www.99-bottles-of-beer.net/language-python-808.html"

    def get_web(self):
        # connect url
        httppool = urllib3.PoolManager()
        # get html
        resultat = httppool.request("GET", self.url)
        # retorn html
        return resultat.data.decode('utf-8')

    def parse_html(self, html):
        # convertir bs4
        soup = bs4.BeautifulSoup(html, features="html.parser")
        # buscar bs4 -> codi
        element_div = soup.find_all('div', attrs={"id":"main"})[0]
        codi = element_div.find_all('pre')[0]
        # retornar codi
        return codi.text

    def get_data(self):
        # descarregar-se web
        dades = self.get_web()
        # llegir html
        dades = self.parse_html(dades)
        # retornar dades
        return dades

if __name__ =="__main__":
    client = Client()
    dades = client.get_data()
    print(dades)
