numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transformados = [x * 2 if x % 2 == 0 else x for x in numeros]
print("Números transformados:", transformados)

#Por ejemplo, la excepción Exception es la clase base para la mayoría
# de las excepciones, y de ella derivan subclases como ArithmeticError 
# y ValueError.
#Comprender esta jerarquía es crucial para poder manejar las excepciones 
# adecuadamente y elegir las excepciones específicas que se desean capturar.
#A continuación se muestra un código que imprime la jerarquía de excepciones
#  en Python:

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)
        # Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)