empleados: list [dict[str, int, float]] = [
                {'name': 'Iris', 'age': 43, 'salary': 100},
                {'name': 'Ivan', 'age': 45, 'salary': 200},
                {'name': 'Andres', 'age': 25, 'salary': 300},
                {'name': 'Nohelia', 'age': 21, 'salary': 400},
                {'name': 'Samuel', 'age': 27, 'salary': 500 },
                {'name': 'David', 'age': 33, 'salary': 600 },
                {'name': 'Sarahi', 'age': 30, 'salary': 700},
                {'name': 'Jesus', 'age': 54, 'salary': 800},
                {'name': 'Haydee', 'age': 34, 'salary': 900},
                {'name': 'Francisco', 'age': 43, 'salary': 1000}
            ] # Variable global

def empleados_filtrados(empleados: list [dict[str, int, float]], sueldo: float) -> list[dict]:
    """Filtra empleados que ganen más de cierto monto.
    A partir de una lista de diccionarios
    El diccionario tiene las variables name: str, age: int y salary: float
    La variable sueldo: float, es el monto del límite que filtra la función
    """
    
    empleados_filtro_sueldo: str = [] # Variable local
    empleados_filtro_sueldo: str = [empleado["name"] for empleado in empleados if empleado["salary"]>= sueldo]
    return empleados_filtro_sueldo
sueldo: float = 900
print(f'Empleados con suledo superior a {sueldo} son:  {empleados_filtrados(empleados, sueldo)}')