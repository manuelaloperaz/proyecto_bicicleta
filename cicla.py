import random

usuarios = []
prestamo = []
cicla = []

bicicletas = ['Bicicleta 1', 'Bicicleta 2', 'Bicicleta 3', 'Bicicleta 4', 'Bicicleta 5']

def registro_usuarios(nombre, cedula, correo):
    usuario = {
        'nombre': nombre,
        'cedula': cedula,
        'correo': correo
    }
    usuarios.append(usuario)

def prestamo_cicla(nombre2, tarjeta, correo2):
    for usuario in usuarios:
        if usuario['nombre'] == nombre2 and usuario['cedula'] == tarjeta and usuario['correo'] == correo2:
            if bicicletas:
                bicicleta_elegida = random.choice(bicicletas)
                bicicletas.remove(bicicleta_elegida)

                destino = input("Destino: ")
                origen = input("Origen: ")
                fecha = input("Fecha: ")

                prestamos = {
                    'nombre2': nombre2,
                    'tarjeta': tarjeta,
                    'correo2': correo2,
                    'bicicleta': bicicleta_elegida,
                    'destino': destino,
                    'origen': origen,
                    'fecha': fecha
                }
                prestamo.append(prestamos)
                print(f"Prestamo exitoso. Se ha asignado la {bicicleta_elegida}.")
            else:
                print("No hay bicicletas disponibles en este momento.")
            return
    print("Usuario no encontrado o datos incorrectos.")

def lista_prestamos():
    if not prestamo:
        print("No hay prestamos en la lista.")
    else:
        for i, prestamos in enumerate(prestamo, 1):
            print(f"Usuario {i}:")
            for usuario in usuarios:
                if usuario['nombre'] == prestamos['nombre2'] and usuario['cedula'] == prestamos['tarjeta'] and usuario['correo'] == prestamos['correo2']:
                    print(f"Nombre: {usuario['nombre']}")
                    print(f"Cedula: {usuario['cedula']}")
                    print(f"Correo: {usuario['correo']}")
                    break

            print(f"Bicicleta asignada: {prestamos['bicicleta']}")
            print(f"Destino: {prestamos['destino']}")
            print(f"Origen: {prestamos['origen']}")
            print(f"Fecha: {prestamos['fecha']}")
            print("")

while True:
    print("Menú:")
    print("1. Registrarse")
    print("2. Prestamo cicla")
    print("3. Listar")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre de usuario: ")
        cedula = input("Cedula: ")
        correo = input("Correo electronico: ")
        registro_usuarios(nombre, cedula, correo)
        print("Registro exitoso")

    elif opcion == "2":
        nombre2 = input("Nombre de usuario: ")
        tarjeta = input("Cedula/tarjeta: ")
        correo2 = input("Correo electronico: ")
        prestamo_cicla(nombre2, tarjeta, correo2)

    elif opcion == "3":
        lista_prestamos()

    elif opcion == "4":
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        print("")
