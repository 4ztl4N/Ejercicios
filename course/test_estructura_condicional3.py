is_member = True
age = 10

if is_member:
    if age>=15:
        print("Tienes acceso ya que eres mayor o igual a 15 años")
    else:
        print("No tienes acceso ya que eres miembro pero no eres mayor a 15 años")
else:
    print("No eres miembro y NO TIENES ACCESO")


usuario1 = "tijera"
usuario2 = "piedra"

if usuario1 == "piedra"and usuario2 == "piedra":
    print("Prueba otra vez")
if usuario1 == "piedra"and usuario2 == "papel":
    print("Usuario 2 GANA")
if usuario1 == "piedra"and usuario2 == "tijera":
    print("Usuario 1 GANA")
if usuario1 == "papel"and usuario2 == "piedra":
    print("Usuario 1 GANA")
if usuario1 == "papel"and usuario2 == "papel":
    print("Prueba otra vez")
if usuario1 == "papel"and usuario2 == "tijera":
    print("Usuario 2 GANA")
if usuario1 == "tijera"and usuario2 == "tijera":
    print("Prueba otra vez")
if usuario1 == "tijera"and usuario2 == "piedra":
    print("Usuario 2 GANA")
if usuario1 == "tijera"and usuario2 == "papel":
    print("Usuario 1 GANA")


