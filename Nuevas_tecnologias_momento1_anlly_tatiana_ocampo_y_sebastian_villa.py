motos = {}


def agregar_moto(marca, modelo):
    motos[marca] = modelo
    print(f"Moto agregada: {marca} - {modelo}")


def mostrar_motos():
    if not motos:
        print("No hay motos registradas.")
    else:
        print("Lista de motos:")
        for marca, modelo in motos.items():
            print(f"{marca} - {modelo}")

def actualizar_moto(marca, nuevo_modelo):
    if marca in motos:
        motos[marca] = nuevo_modelo
        print(f"Moto actualizada: {marca} - {nuevo_modelo}")
    else:
        print(f"{marca} no encontrada. No se puede actualizar.")

def eliminar_moto(marca):
    if marca in motos:
        del motos[marca]
        print(f"Moto eliminada: {marca}")
    else:
        print(f"{marca} no encontrada. No se puede eliminar.")


while True:
    print("\nSeleccione una opción:")
    print("1. Agregar Moto")
    print("2. Mostrar Motos")
    print("3. Actualizar Moto")
    print("4. Eliminar Moto")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        marca = input("Ingrese la marca de la moto: ")
        modelo = input("Ingrese el modelo de la moto: ")
        agregar_moto(marca, modelo)
    elif opcion == "2":
        mostrar_motos()
    elif opcion == "3":
        marca = input("Ingrese la marca de la moto a actualizar: ")
        nuevo_modelo = input("Ingrese el nuevo modelo: ")
        actualizar_moto(marca, nuevo_modelo)
    elif opcion == "4":
        marca = input("Ingrese la marca de la moto a eliminar: ")
        eliminar_moto(marca)
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
