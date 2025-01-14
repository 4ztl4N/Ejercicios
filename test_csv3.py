import csv

file_path = "products_updated.csv"
updated_file_path = "products.csv"

with open(file_path, mode = "r") as file:
    csv_reader = csv.DictReader(file)
    #Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ["total_value"] + ['30%_discount_price']

    with open(updated_file_path, mode = "w", newline="") as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader() #Escribe encabezado

        for row in csv_reader:
            row["total_value"] = float(row["price"]) * int(row["quantity"])
            row['30%_discount_price'] = float(row['price'])*float(0.70)
            csv_writer.writerow(row)

            

        
      
