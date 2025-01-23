import json
import csv

#Leer archivo Json
with open("products.json", mode= "r") as file:
    products = json.load(file)

#Escribir el archivo CSV
with open("products_change.csv", mode="w", newline="") as update_file:
    #Obtener los encabezados desde las claves del primer diccionario
    fielnames = products[0].keys()
    csv_writer = csv.DictWriter(update_file, fieldnames=fielnames)
    csv_writer.writeheader() #Escribir los encabezados
    for row in products:
        csv_writer.writerow(row)
        