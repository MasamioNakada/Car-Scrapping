from bs4 import BeautifulSoup
import requests
import os
import csv

def link_register(link:str):
    if not (os.path.exists("links.csv")):
        field = ["link"]
        with open("links.csv","a") as f:
            writer = csv.writer(f)
            writer.writerow(field)
    
    with open(r"links.csv","a") as f:
        writer = csv.writer(f)
        writer.writerow([link])

def get_links(get_all:str="False"):
    link_list = []
    counter = 0
    if get_all == "True": 
        for page in range(368 + 1):
            r = requests.get(f"https://neoauto.com/venta-de-autos-usados?page={page}").text
            soup_t = BeautifulSoup(r,'lxml')
            car_list = soup_t.find_all('a',attrs={'class':'c-results-use__link'})
            for car in car_list:
                counter += 1
                print(f"Page: {page}, append: {counter} page")
                link = f'https://neoauto.com/{car["href"]}'
                link_list.append(link)
                link_register(link)

    else:
        r = requests.get("https://neoauto.com/venta-de-autos-usados?page=1").text
        soup_t = BeautifulSoup(r,"lxml")
        car_list = soup_t.find_all('a',attrs={'class':'c-results-use__link'})
        for car in car_list:
            counter += 1
            print(f"Page: 1, append: {counter} page")
            link = f'https://neoauto.com/{car["href"]}'
            link_list.append(link)
            link_register(link)
    
    return link_list 