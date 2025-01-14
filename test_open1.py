#Leer un archivo lína por línea

"""with open("cuento.txt","r") as file:
    for lineas in file:
        print(lineas.strip())"""

#Leer todas las líneas en una lista
"""with open("cuento.txt","r") as file:
    lines = file.readlines()
    print(lines)"""

#Añadir texto al archivo TXT"
"""with open("cuento.txt","a") as file:
    file.write("\n\nBy: Chat GPT")"""

#Sobreescribir archivo TXT, esto borra lo que tiene y solo deja lo que aquí pongas
#por lo que se deberá tener cuidado al usarlo
"""with open("cuento.txt","w") as file:
    file.write("\n\nBy: Chat GPT")"""

#Reto conteo de líneas
# contar el numero de lineas de un archivo txt

file = open('cuento.txt', 'r')
lines = file.readlines()
n_lines = 0

for line in lines:
    n_lines += 1
print(f"el cuento del archivo tiene {n_lines} lineas")
file.close()

with open('cuento.txt', 'r') as file:
    lines = file.readlines()
    print(f'El total de lineas del archivo es: {len(lines)}')
