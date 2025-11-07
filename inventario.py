

# Bucle para pedir el nombre del producto
while True:
    nombre = input("Ingrese el nombre del producto: ")
    
    # Verificamos que el nombre solo tenga letras (sin números ni símbolos)
    if not nombre.isalpha():
        print("Ingrese un nombre valido por favor")
        continue  # vuelve a pedir el dato si no cumple
    break  # sale del ciclo si el dato es correcto


# Bucle para pedir el precio del producto
while True:
    try:
        # Se intenta convertir el valor a tipo float (decimal)
        precio = float(input(f"Ingrese el precio del producto ({nombre}): "))
        
        # Validamos que el precio sea mayor que cero
        if (precio <= 0):
            print("Ingrese un precio valido, no numeros negativos")
            continue  # vuelve a pedir el precio si no cumple
        
    # Si el usuario ingresa texto u otro valor no numérico, da error
    except ValueError:
        print("Ingrese un precio valido")
        continue  # vuelve a pedir el dato
    
    break  # sale del ciclo si todo está bien


# Bucle para pedir la cantidad del producto
while True:
    try:
        # Se intenta convertir el valor a entero
        cantidad = int(input(f"Ingrese la cantidad que hay del producto ({nombre}): "))
        
        # Validamos que la cantidad sea positiva
        if (cantidad <= 0):
            print("Ingrese una cantidad valida, no numeros negativos")
            continue
        
    # Si el usuario no ingresa un número entero, muestra el mensaje de error
    except ValueError:
        print("Ingrese una cantidad valida ")
        continue
    
    break  # sale del ciclo si el dato es correcto


# Calculamos el costo total multiplicando precio * cantidad
costo_total = precio * cantidad


# Mostramos los datos en formato de tabla
print("")
print("-" * 50)
print("{:<15} | {:<10} | {:<5} | {}".format("Producto", "Precio", "Cantidad", "Total"))
print("{:<15} | {:<10,.0f} | {:<8} | {:,.0f}".format(nombre, precio, cantidad, costo_total))
print("-" * 50)