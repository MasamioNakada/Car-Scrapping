import csv  
import os
#import sqlite3

from extract_from_link import ExtractNeoAutos

#conn = sqlite3.connect('database.db')
#cursor = conn.cursor()
#
#cursor.execute('''
#        CREATE TABLE IF NOT EXISTS report(
#            id INTEGER PRIMARY KEY,
#            title TEXT,
#            price REAL,
#            description TEXT,
#            year_manufacture INTEGER,
#            km REAL,
#            transmission TEXT,
#            fuel TEXT,
#            cc REAL,
#            placa TEXT,
#            category TEXT,
#            brand TEXT,
#            model_name TEXT,
#            number_doors INTEGER,
#            traction TEXT,
#            color TEXT,
#            n_cilinders INTEGER
#)''')
#
class SaveData():
    def __init__(self,link_list:list) -> None:

        report_list_list = []
        for link in link_list:
            print(f"Processing {link}")
            ex = ExtractNeoAutos(link)
            re = ex.get_all()

            try:
                price = float(re['price'].replace(",",""))
            except:
                price = "None"
            
            try:
                km = float(re["Kilometraje"][:-3].replace(",",""))
            except:
                km = "None"

            try:
                cc = float(re["Cilindrada"][:-3].replace(",",""))
            except:
                cc = "None"
            
            clean_re  = { "title":re['title'],
                        "price":price, 
                        "description":re["description"],
                        "Año de fabricación": re["Año Modelo"],
                        "Kilometraje":km,
                        "Transmisión":re["Transmisión"],
                        "Combustible":re["Combustible"],
                        "Cilindrada":cc,
                        "Placa":re["Placa"],
                        "Categoría":re["Categoría"],
                        "Marca":re["Marca"],
                        "Modelo":re["Modelo"],
                        "Número de puertas":re["Número de puertas"],
                        "Tracción":re["Tracción"],
                        "Color":re["Color"],
                        "Número cilindros":re["Número cilindros"]}
            
            report_list_list.append( list(clean_re.values()))
        self.report_list_list = report_list_list

            
    def save_csv(self):
        if not (os.path.exists("data.csv")):
            fields=['title',
             'price',
             'description',
             'Año de fabricación',
             'Kilometraje',
             'Transmisión',
             'Combustible',
             'Cilindrada',
             'Placa',
             'Categoría',
             'Marca',
             'Modelo',
             'Número de puertas',
             'Tracción',
             'Color',
             'Número cilindros']
            with open(r'data.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(fields)

        with open(r'data.csv', 'a') as f:
            writer = csv.writer(f)
            for report_list in self.report_list_list:
                writer.writerow(report_list)
        return True

#    def save_db(self):
#        for report_list in self.report_list_list:
#            print(report_list)
#            cursor.execute(''' INSERT INTO 
#                    report(title,price,description,year_manufacture,km,transmission,fuel,cc,placa,category,brand,model_name,number_doors,traction,color,n_cilinders) 
#                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
#                    ,report_list)
#
#            conn.commit()
#        conn.close()
#        return True
   
        

#def save_csv(link_list:list):
#    for link in link_list:
#        print(link)
#        ex = ExtractNeoAutos(link)
#        re = ex.get_all()
#        clean_re  = { "title":re['title'],
#                    "price":float(re['price'].replace(",","")), 
#                    "description":re["description"],
#                    "Año de fabricación": re["Año Modelo"],
#                    "Kilometraje":float(re["Kilometraje"][:-3].replace(",","")),
#                    "Transmisión":re["Transmisión"],
#                    "Combustible":re["Combustible"],
#                    "Cilindrada":float(re["Cilindrada"][:-3].replace(",","")),
#                    "Placa":re["Placa"],
#                    "Categoría":re["Categoría"],
#                    "Marca":re["Marca"],
#                    "Modelo":re["Modelo"],
#                    "Año de fabricación":re["Año de fabricación"],
#                    "Número de puertas":re["Número de puertas"],
#                    "Tracción":re["Tracción"],
#                    "Color":re["Color"],
#                    "Número cilindros":re["Número cilindros"]}
#        with open(r'data.csv', 'a') as f:
#            writer = csv.writer(f)
#            writer.writerow(list(clean_re.values()))
#    return True

#def save_db(link_list:list):
#    for link in link_list:
#        print(link)
#        ex = ExtractNeoAutos(link)
#        re = ex.get_all()
#        clean_re  = { "title":re['title'],
#                    "price":float(re['price'].replace(",","")), 
#                    "description":re["description"],
#                    "year_manufacture": re["Año Modelo"],
#                    "km":float(re["Kilometraje"][:-3].replace(",","")),
#                    "transmission":re["Transmisión"],
#                    "fuel":re["Combustible"],
#                    "cc":float(re["Cilindrada"][:-3].replace(",","")),
#                    "placa":re["Placa"],
#                    "Categoría":re["Categoría"],
#                    "Marca":re["Marca"],
#                    "Modelo":re["Modelo"],
#                    "Año de fabricación":re["Año de fabricación"],
#                    "Número de puertas":re["Número de puertas"],
#                    "Tracción":re["Tracción"],
#                    "Color":re["Color"],
#                    "Número cilindros":re["Número cilindros"]}
#        cursor.execute(''' INSERT INTO 
#        report(title,price,description,year_manufacture,km,transmission,fuel,cc,placa,category,brand,model_name,year_created,number_doors,traction,color,n_cilinders) 
#        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
#        ,list(clean_re.values()))
#
#        conn.commit()
#    conn.close()
#    return True
#
