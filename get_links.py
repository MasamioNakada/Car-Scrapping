from bs4 import BeautifulSoup
import requests

def get_links(get_all:bool=False):
    link_list = []
    counter = 0
    if get_all: 
        for page in range(368 + 1):
            r = requests.get(f"https://neoauto.com/venta-de-autos-usados?page={page}").text
            soup_t = BeautifulSoup(r,'lxml')
            car_list = soup_t.find_all('a',attrs={'class':'c-results-use__link'})
            for car in car_list:
                counter += 1
                print(f"Page: {page}, append: {counter} page")
                link_list.append(f'https://neoauto.com/{car["href"]}')

    else:
        r = requests.get("https://neoauto.com/venta-de-autos-usados?page=1").text
        soup_t = BeautifulSoup(r,"lxml")
        car_list = soup_t.find_all('a',attrs={'class':'c-results-use__link'})
        for car in car_list:
            link_list.append(f'https://neoauto.com/{car["href"]}')
    
    return link_list 