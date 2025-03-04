# Primera función: recibe la información de los empleados
def informacion_empleados(diccionario_empleados):
    empleados = []
    for clave, valor in diccionario_empleados.items():
        empleados.append(valor)
    return empleados

# Segunda función: analiza los empleados y devuelve aquellos que ganan un cierto monto
def empleados_con_salario_superior(empleados, monto):
    empleados_filtrados = [empleado for empleado in empleados if empleado["salario"] >= monto]
    return empleados_filtrados

diccionario_empleados = {
    1: {"nombre": "Juan", "edad": 30, "salario": 50000},
    2: {"nombre": "María", "edad": 25, "salario": 60000},
    3: {"nombre": "Pedro", "edad": 35, "salario": 40000}
}

empleados = informacion_empleados(diccionario_empleados)
monto = 50000
empleados_filtrados = empleados_con_salario_superior(empleados, monto)

print("Empleados que ganan {} o más:".format(monto))
for empleado in empleados_filtrados:
    print(empleado)