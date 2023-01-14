from bs4 import BeautifulSoup
import requests

class ExtractNeoAutos():
    def __init__(self,link:str) -> "None":
        r = requests.get(link).text
        self.soup = BeautifulSoup(r,'lxml')
    def title(self):
        return self.soup.find('h1',attrs={'class':'sc-813e4f1-0 sc-6cde9968-0 fstToR NLmIK'}).text

    def price(self):
        return self.soup.find('p',attrs={'class':'sc-813e4f1-0 sc-c1459997-0 fstToR dYanzN'}).text[4:]

    def description(self):
        return self.soup.find('pre', attrs={'class':'sc-c8f2aade-1 hJykuS'}).text

    def user_use(self):
        usability_keys = self.soup.find_all('div',attrs={'class':'sc-11692204-2 idSOrq'})
        usability_keys_list = []
        for div in usability_keys:
            usability_keys_list.append(div.text)

        use = self.soup.find_all('div',attrs={'class':'sc-11692204-3 htOtEa'})
        user_values = []
        for div in use:
            user_values.append(div.text)

        return dict(zip(usability_keys_list, user_values))
 
    def specs(self):
        specs_keys = self.soup.find_all('div',attrs={'class':'sc-25b7b222-1 cLLifQ'})
        specs_keys_list = []
        for div in specs_keys:
            specs_keys_list.append(div.text)

        specs = self.soup.find_all('div',attrs={'class':'sc-25b7b222-2 jhOymW'})

        specs_values = []
        for div in specs:
            specs_values.append(div.text)

        return dict(zip(specs_keys_list, specs_values))

    def get_all(self):
        report = {}
        report['title'] = self.title()
        report['price'] = self.price()
        report['description'] = self.description()
        report.update(self.user_use())
        report.update(self.specs())

        report.setdefault('title', "None")
        report.setdefault('price', "None")
        report.setdefault('description', "None")
        report.setdefault('Año Modelo', "None")
        report.setdefault('Kilometraje', "None")
        report.setdefault('Transmisión', "None")
        report.setdefault('Combustible', "None")
        report.setdefault('Cilindrada', "None")
        report.setdefault('Placa', "None")
        report.setdefault('Categoría', "None")
        report.setdefault('Marca', "None")
        report.setdefault('Modelo', "None")
        report.setdefault('Número de puertas', "None")
        report.setdefault('Tracción', "None")
        report.setdefault('Color', "None")
        report.setdefault('Número cilindros', "None")

        return report


  
