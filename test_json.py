import json

#Lectura del archivo Jason
with open("products.json", mode="r") as file:
    products = json.load(file)

#Mostrar el contenido
for product in products:
    #print(product)
    print(f"Product: {product["name"]}, Price: {product["price"]}")