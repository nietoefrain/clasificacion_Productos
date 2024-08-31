while True:
    try:
        codigo_producto = input("Ingrese el código de tipo de producto (A, B, C): ").upper()
        if codigo_producto in ('A', 'B', 'C'):
            if codigo_producto == 'A':
                tipo_producto = "Producto Alimenticio"
            elif codigo_producto == 'B':
                tipo_producto = "Producto Electronico"
            elif codigo_producto == 'C':
                tipo_producto = "Otros Productos"
            break
        else:
            print("Codigo Invalido. Por favor, ingrese 'A', 'B' o 'C'")
    except ValueError:
        print("Valor inválido. Por favor, ingrese un valor de la lista 'A', 'B' o 'C'.")

while True:
    try:
        peso_producto = float(input("Ingrese el peso del producto (Kg): "))
        if peso_producto > 0:
            if peso_producto >= 20:
                categoria_peso = "Pesado"
            elif 10 <= peso_producto < 20:
                categoria_peso = "Mediano"
            elif peso_producto < 10:
                categoria_peso = "Ligero"
            break
        else:
            print("Valor inválido. El peso debe ser un número positivo mayor a cero.")
    except ValueError:
        print("Valor inválido. Por favor, ingrese un valor numérico válido.")

while True:
    fragilidad = input('Ingrese la fragilidad del producto ("F" = Frágil, "N" = No Frágil): ').upper()
    if fragilidad in ('F', 'N'):
        if fragilidad == "F":
            tipo_fragilidad = "Fragil"
        elif fragilidad == "N":
            tipo_fragilidad = "No fragil"
        break
    else:
        print('Valor inválido. La fragilidad debe ser un valor de la lista ("F" = Frágil, "N" = No Frágil).')


def clasificacion_final(codigo_producto, categoria_peso, tipo_fragilidad):
    if codigo_producto == "A":
        if categoria_peso == "Pesado" and tipo_fragilidad == "Fragil":
            print(f"{tipo_producto} {categoria_peso} y {tipo_fragilidad}: Manejar con extremo cuidado")
        elif categoria_peso == "Mediano" and tipo_fragilidad == "Fragil":
            print(f"{tipo_producto} {categoria_peso} y {tipo_fragilidad}: Manejar con cuidado")
        elif categoria_peso == "Ligero":
            print(f"{tipo_producto} {categoria_peso} y {tipo_fragilidad}: Manejar con cuidado estandar.")
    elif codigo_producto == "B":
        if tipo_fragilidad == "Fragil":
            print(f"{tipo_producto} {tipo_fragilidad}: Manejar con cuidado.")
        elif tipo_fragilidad == "No fragil" and categoria_peso == "Pesado":
            print(f"{tipo_producto} {categoria_peso} y {tipo_fragilidad}: Manejar con precaucion")
        elif tipo_fragilidad == "No fragil" and categoria_peso in ("Mediano", "Ligero"):
            print(f"{tipo_producto} {tipo_fragilidad}: Manejo estandar")
    elif codigo_producto == "C":
        if categoria_peso == "Pesado" and tipo_fragilidad == "Fragil":
            print(F"Producto {categoria_peso} y {tipo_fragilidad} : Manejar con precaucion adicional")
        elif categoria_peso == "Pesado" and tipo_fragilidad == "No fragil":
            print(F"Producto {categoria_peso} y {tipo_fragilidad} : Manejo standar.")
        elif categoria_peso in ("Mediano", "Ligero"):
            print(f"Producto no pesado: Manejo standar")

clasificacion_final(codigo_producto, categoria_peso, tipo_fragilidad)

