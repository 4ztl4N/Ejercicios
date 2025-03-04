

square = [x**2 for x in range(1, 15)]
print(square)


transformados = [x * 2 if x % 2 == 0 else x for x in range(1,20)]
print("Números transformados:", transformados)
