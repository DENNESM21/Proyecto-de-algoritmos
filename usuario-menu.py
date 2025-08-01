import random
from collections import deque

# Función para cargar ninjas desde archivo ninjas.txt
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
        print("Archivo 'ninjas.txt' no encontrado.")
    return ninjas

# 1. Ver árbol de habilidades de un ninja
def ver_arbol_habilidades():
    nombre_ninja = input("Nombre del ninja: ").strip()
    try:
        with open("habilidades_ninja.txt", "r") as f:
            for linea in f:
                if linea.startswith(nombre_ninja + ":"):
                    habilidades = linea.strip().split(":")[1].split(",")
                    print(f"\nÁrbol de habilidades de {nombre_ninja}:")
                    for h in habilidades:
                        print("→", h)
                    return
        print("Ninja no encontrado.")
    except FileNotFoundError:
        print("Archivo 'habilidades_ninja.txt' no existe.")

# 2. Simular combate 1 vs 1
def simular_combate(usuario_email):
    ninjas = cargar_ninjas()
    if len(ninjas) < 2:
        print("No hay suficientes ninjas para combatir.")
        return

    print("Ninjas disponibles:")
    for i, n in enumerate(ninjas):
        print(f"{i+1}. {n['nombre']}")

    try:
        i1 = int(input("Elige el número del primer ninja: ")) - 1
        i2 = int(input("Elige el número del segundo ninja: ")) - 1
        if i1 == i2 or i1 not in range(len(ninjas)) or i2 not in range(len(ninjas)):
            print("Selección inválida.")
            return
    except ValueError:
        print("Debes ingresar números válidos.")
        return

    n1, n2 = ninjas[i1], ninjas[i2]

    poder1 = n1['fuerza'] + n1['agilidad'] + n1['resistencia'] + random.randint(0, 10)
    poder2 = n2['fuerza'] + n2['agilidad'] + n2['resistencia'] + random.randint(0, 10)

    print(f"\n{n1['nombre']} VS {n2['nombre']}")
    print(f"Poder total: {poder1} vs {poder2}")

    if poder1 > poder2:
        ganador = n1['nombre']
    elif poder2 > poder1:
        ganador = n2['nombre']
    else:
        ganador = "Empate"

    print(f"Ganador: {ganador}")

    with open("combates.txt", "a") as f:
        f.write(f"{n1['nombre']} vs {n2['nombre']} – Ganador: {ganador}\n")

    with open(f"combates_{usuario_email}.txt", "a") as f:
        f.write(f"{n1['nombre']} vs {n2['nombre']} – Ganador: {ganador}\n")

# 3. Simular torneo completo (2,4,8,16, etc ninjas)
def simular_torneo(usuario_email):
    ninjas = cargar_ninjas()
    n = len(ninjas)
    if n < 2 or (n & (n - 1)) != 0:
        print("El torneo requiere 2, 4, 8, 16, etc. ninjas.")
        return

    ronda = 1
    cola = deque(ninjas)
    resultados = []

    while len(cola) > 1:
        print(f"\nRONDA {ronda}:")
        nuevos = deque()
        while len(cola) >= 2:
            n1 = cola.popleft()
            n2 = cola.popleft()
            poder1 = n1['fuerza'] + n1['agilidad'] + n1['resistencia'] + random.randint(0, 10)
            poder2 = n2['fuerza'] + n2['agilidad'] + n2['resistencia'] + random.randint(0, 10)

            if poder1 > poder2:
                ganador = n1
            else:
                ganador = n2

            print(f"{n1['nombre']} vs {n2['nombre']} → Ganador: {ganador['nombre']}")
            resultados.append(f"{n1['nombre']} vs {n2['nombre']} – Ganador: {ganador['nombre']}")
            nuevos.append(ganador)

        cola = nuevos
        ronda += 1

    campeon = cola.popleft()
    print(f"\nCAMPEÓN DEL TORNEO: {campeon['nombre']}")

    with open("combates.txt", "a") as f:
        for linea in resultados:
            f.write(linea + "\n")

    with open(f"combates_{usuario_email}.txt", "a") as f:
        for linea in resultados:
            f.write(linea + "\n")

# 4. Mostrar ranking de ninjas por victorias
def mostrar_ranking():
    victorias = {}

    try:
        with open("combates.txt", "r") as f:
            for linea in f:
                if "Ganador:" in linea:
                    partes = linea.strip().split("Ganador:")
                    ganador = partes[1].strip()
                    if ganador != "Empate":
                        victorias[ganador] = victorias.get(ganador, 0) + 1
    except FileNotFoundError:
        print("No hay combates registrados aún.")
        return

    if not victorias:
        print("Aún no hay victorias registradas.")
        return

    print("\nRANKING DE NINJAS POR VICTORIAS:")
    ranking = sorted(victorias.items(), key=lambda x: x[1], reverse=True)
    for pos, (ninja, puntos) in enumerate(ranking, start=1):
        print(f"{pos}. {ninja} - {puntos} victorias")

# 5. Mostrar historial de un usuario
def mostrar_historial(usuario_email):
    try:
        with open(f"combates_{usuario_email}.txt", "r") as f:
            print("\nHISTORIAL DE COMBATES:")
            print(f.read())
    except FileNotFoundError:
        print("No hay historial para este jugador.")

# Menú principal para jugador
def menu_jugador(usuario_email):
    while True:
        print(f"\n=== MENÚ DEL JUGADOR ({usuario_email}) ===")
        print("1. Ver árbol de habilidades de un ninja")
        print("2. Simular combate uno vs uno")
        print("3. Simular torneo completo")
        print("4. Ver ranking actualizado")
        print("5. Ver mi historial personal")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ver_arbol_habilidades()
        elif opcion == "2":
            simular_combate(usuario_email)
        elif opcion == "3":
            simular_torneo(usuario_email)
        elif opcion == "4":
            mostrar_ranking()
        elif opcion == "5":
            mostrar_historial(usuario_email)
        elif opcion == "6":
            print("Saliendo del menú del jugador.")
            break
        else:
            print("Opción inválida.")

# Para probar el menú, cambia el email aquí:
if __name__ == "__main__":
    usuario_email = input("Ingresa tu email de usuario: ").strip()
    menu_jugador(usuario_email)
