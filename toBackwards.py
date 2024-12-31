#Instrucciones
#Crea una función que retorne la cadena de texto al revés.

def palindromo(original):
    if(original == None): return False
    if(type(original) != str): return False
    reves=[]
    for letra in original[::-1]:
        reves.append(letra)
    
    palabra_reves= ''.join(reves)
    return palabra_reves == original

def palindrom(original): return original[::-1] == original