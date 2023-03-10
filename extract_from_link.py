from bs4 import BeautifulSoup
import requests

class ExtractNeoAutos():
    def __init__(self,link:str) ->None:
        r = requests.get(link).text
        self.soup = BeautifulSoup(r,'lxml')
    def title(self):
        try:
            return self.soup.find('h1',attrs={'class':'sc-813e4f1-0 sc-6cde9968-0 fstToR NLmIK'}).text
        except:
            return None

    def price(self):
        try:
            return self.soup.find('p',attrs={'class':'sc-813e4f1-0 sc-c1459997-0 fstToR dYanzN'}).text[4:]
        except:
            return None

    def description(self):
        try:
            return self.soup.find('pre', attrs={'class':'sc-c8f2aade-1 hJykuS'}).text
        except:
            return None

    def user_use(self) -> dict :
        try:
            usability_keys = self.soup.find_all('div',attrs={'class':'sc-11692204-2 idSOrq'})
            usability_keys_list = []
            for div in usability_keys:
                usability_keys_list.append(div.text)
            try:
                use = self.soup.find_all('div',attrs={'class':'sc-11692204-3 htOtEa'})
            except:
                use = []

            user_values = []
            for div in use:
                user_values.append(div.text)

            return dict(zip(usability_keys_list, user_values))
        except:
            return {}
 
    def specs(self) -> dict:
        try:
            specs_keys = self.soup.find_all('div',attrs={'class':'sc-25b7b222-1 cLLifQ'})
            specs_keys_list = []
            for div in specs_keys:
                specs_keys_list.append(div.text)
            try:
                specs = self.soup.find_all('div',attrs={'class':'sc-25b7b222-2 jhOymW'})
            except:
                specs = []

            specs_values = []
            for div in specs:
                specs_values.append(div.text)

            return dict(zip(specs_keys_list, specs_values))
        except:
            return {}

    def get_all(self):
        report = {}
        report['title'] = self.title()
        report['price'] = self.price()
        report['description'] = self.description()
        report.update(self.user_use())
        report.update(self.specs())

        report.setdefault('title',None)
        report.setdefault('price',None)
        report.setdefault('description',None)
        report.setdefault('A??o Modelo',None)
        report.setdefault('Kilometraje',None)
        report.setdefault('Transmisi??n',None)
        report.setdefault('Combustible',None)
        report.setdefault('Cilindrada',None)
        report.setdefault('Placa',None)
        report.setdefault('Categor??a',None)
        report.setdefault('Marca',None)
        report.setdefault('Modelo',None)
        report.setdefault('N??mero de puertas',None)
        report.setdefault('Tracci??n',None)
        report.setdefault('Color',None)
        report.setdefault('N??mero cilindros',None)

        return report


  
