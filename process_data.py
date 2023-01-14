import csv  
import sqlite3
from extract_from_link import ExtractNeoAutos

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS report(
            id INTEGER PRIMARY KEY,
            title TEXT,
            price REAL,
            description TEXT,
            year_manufacture INTEGER,
            km REAL,
            transmission TEXT,
            fuel TEXT,
            cc REAL,
            placa TEXT,
            category TEXT,
            brand TEXT,
            model_name TEXT,
            year_created INTEGER,
            number_doors INTEGER,
            traction TEXT,
            color TEXT,
            n_cilinders INTEGER
)
''')

def save_csv(link_list:list):
    for link in link_list:
        print(link)
        ex = ExtractNeoAutos(link)
        re = ex.get_all()
        clean_re  = { "title":re['title'],
                    "price":float(re['price'].replace(",","")), 
                    "description":re["description"],
                    "Año de fabricación": re["Año Modelo"],
                    "Kilometraje":float(re["Kilometraje"][:-3].replace(",","")),
                    "Transmisión":re["Transmisión"],
                    "Combustible":re["Combustible"],
                    "Cilindrada":float(re["Cilindrada"][:-3].replace(",","")),
                    "Placa":re["Placa"],
                    "Categoría":re["Categoría"],
                    "Marca":re["Marca"],
                    "Modelo":re["Modelo"],
                    "Año de fabricación":re["Año de fabricación"],
                    "Número de puertas":re["Número de puertas"],
                    "Tracción":re["Tracción"],
                    "Color":re["Color"],
                    "Número cilindros":re["Número cilindros"]}
        with open(r'data.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(list(clean_re.values()))
    return True

def save_db(link_list:list):
    for link in link_list:
        print(link)
        ex = ExtractNeoAutos(link)
        re = ex.get_all()
        clean_re  = { "title":re['title'],
                    "price":float(re['price'].replace(",","")), 
                    "description":re["description"],
                    "year_manufacture": re["Año Modelo"],
                    "km":float(re["Kilometraje"][:-3].replace(",","")),
                    "transmission":re["Transmisión"],
                    "fuel":re["Combustible"],
                    "cc":float(re["Cilindrada"][:-3].replace(",","")),
                    "placa":re["Placa"],
                    "Categoría":re["Categoría"],
                    "Marca":re["Marca"],
                    "Modelo":re["Modelo"],
                    "Año de fabricación":re["Año de fabricación"],
                    "Número de puertas":re["Número de puertas"],
                    "Tracción":re["Tracción"],
                    "Color":re["Color"],
                    "Número cilindros":re["Número cilindros"]}
        cursor.execute(''' INSERT INTO 
        report(title,price,description,year_manufacture,km,transmission,fuel,cc,placa,category,brand,model_name,year_created,number_doors,traction,color,n_cilinders) 
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        ,list(clean_re.values()))

        conn.commit()
    conn.close()
    return True

