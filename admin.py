def cargar_ninjas():
    ninjas = []
    try:
        with open("ninjas.txt", "r") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) == 6:
                    nombre, fuerza, agilidad, resistencia, estilo, puntos = partes
                    ninjas.append({
                        "nombre": nombre,
                        "fuerza": int(fuerza),
                        "agilidad": int(agilidad),
                        "resistencia": int(resistencia),
                        "estilo": estilo,
                        "puntos": int(puntos)
                    })
    except FileNotFoundError:
        # Si el archivo no existe, lo crea vacío
        with open("ninjas.txt", "w") as f:
            pass  # No escribe nada aún, solo crea el archivo
        print("Archivo 'ninjas.txt' se acaba de crear")

    return ninjas

def guardar_ninjas(ninjas):
    with open("ninjas.txt", "w") as f:
        for ninja in ninjas:
            f.write(f"{ninja['nombre']},{ninja['fuerza']},{ninja['agilidad']},{ninja['resistencia']},{ninja['estilo']},{ninja['puntos']}\n")

def menu_admin():
    ninjas = cargar_ninjas()

    while True:
        print("\n=== MENÚ ADMINISTRADOR ===")
        print("1. Agregar ninja")
        print("2. Listar ninjas")
        print("3. Buscar ninja por nombre")
        print("4. Actualizar ninja")
        print("5. Eliminar ninja")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            fuerza = int(input("Fuerza: "))
            agilidad = int(input("Agilidad: "))
            resistencia = int(input("Resistencia: "))
            estilo = input("Estilo de pelea: ")
            puntos = int(input("Puntos: "))
            ninjas.append({
                "nombre": nombre,
                "fuerza": fuerza,
                "agilidad": agilidad,
                "resistencia": resistencia,
                "estilo": estilo,
                "puntos": puntos
            })
            guardar_ninjas(ninjas)
            print("Ninja agregado.")

        elif opcion == "2":
            print("Lista de ninjas:\n")
            for ninja in ninjas:
                print(f"{ninja['nombre']} - {ninja['estilo']} - Puntos: {ninja['puntos']}")

        elif opcion == "3":
            buscar = input("Nombre del ninja que desea buscar: ").lower()
            encontrados = [n for n in ninjas if buscar in n['nombre'].lower()]
            if encontrados:
                for ninja in encontrados:
                    print(ninja)
            else:
                print("No se ha encontrado")

        elif opcion == "4":
            nombre = input("Nombre del ninja que desea actualizar: ")
            for ninja in ninjas:
                if ninja['nombre'].lower() == nombre.lower():
                    ninja['fuerza'] = int(input("Nueva fuerza: "))
                    ninja['agilidad'] = int(input("Nueva agilidad: "))
                    ninja['resistencia'] = int(input("Nueva resistencia: "))
                    ninja['estilo'] = input("Nuevo estilo: ")
                    ninja['puntos'] = int(input("Nuevos puntos: "))
                    guardar_ninjas(ninjas)
                    print("Se ha actualizado el Ninja")
                    break
            else:
                print("No se encontró")

        elif opcion == "5":
            nombre = input("Nombre del ninja que desea eliminar: ")
            for i, ninja in enumerate(ninjas):
                if ninja['nombre'].lower() == nombre.lower():
                    del ninjas[i]
                    guardar_ninjas(ninjas)
                    print("Ninja eliminado")
                    break
            else:
                print("No se encontró")

        elif opcion == "6":
            break
        else:
            print("Ingrese un dígito correcto")
