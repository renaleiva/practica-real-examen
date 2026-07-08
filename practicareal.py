

def validar_titulo():
    while True:
        titulo = input("Ingrese el titulo de la cancion: ")
        if titulo.strip() == "":
            print("Error: El titulo no puede estar vacio ni contener espacios.")
        else:
            return titulo
        
def validar_anio():
    while True:
        try:
            anio_numero = int(input("Ingrese el año de lanzamiento de la cancion: "))
            if anio_numero > 1950:
                return anio_numero
            else:
                print("El año debe ser mayor a 1950")
        except ValueError:
            print("Error: Debe ingresar un numero entero valido para el año")

def validar_duracion():
    while True:
        try:
            duracion = float(input("Ingrese la duracion de la cancion: "))
            if 0.5 <= duracion <= 15.0:
                return duracion
            else:
                print("La duracion debe estar entre 05 y 15.0")
        except ValueError:
            print("El numero debe ser decimal valido.") 

def mostrar_menu():
    print("=====MENU PRINCIPAL=====")
    print("1. Agregar cancion")
    print("2. Buscar cancion")
    print("3. Eliminar cancion")
    print("4. Actualizar esatdos")
    print("5. Mostrar canciones")
    print("6. Salir")
    print("========================")

def pedir_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion entre el 1 y el 6: "))
            if 1<= opcion <=6:
                return opcion
            else:
                print("El numero debe estar entre el 1 y el 6")
        except ValueError:
            print("Error: La opcion debe ser un numero entero valido.")


def agregar_cancion(lista):
    print("AGREGAR CANCION")

    titulo = validar_titulo()
    anio = validar_anio()
    duracion = validar_duracion()

    nueva_cancion = {
        "titulo": titulo,
        "anio": anio,
        "duracion": duracion,
        "en_rotacion": False
    }

    lista.append(nueva_cancion)
    print(f"La cancion '{titulo}' fue agregada con exito")


def buscar_cancion(lista, titulo_buscar):
    for posicion in range(len(lista)):
        if lista[posicion]["titulo"].lower() == titulo_buscar.lower():
            return posicion
    return -1

def eliminar_cancion(lista):
    print("ELIMINAR CANCION")
    titulo = input("Ingrese el titulo de la cancion que desea eliminar: ")
    posicion = buscar_cancion(lista, titulo)
    if posicion != -1:
        lista.pop(posicion)
        print(f"La cancion '{titulo}' ha sido eliminada con exito")
    else:
        print(f"La cancion '{titulo}' no se encuentra registrada")

def actualizar_estados(lista):
    for cancion in lista:
        if cancion["anio"] >= 2020:
            cancion["en_rotacion"] = True
        else:
            cancion["en_rotacion"] = False

def mostrar_canciones(lista):
    actualizar_estados(lista)

    print("LISTA DE CANCIONES")

    if len(lista) == 0:
        print("No se registraron canciones")
        return
    for cancion in lista:
        if cancion["en_rotacion"]:
            estado_texto = "EN ROTACION"
        else:
            estado_texto = "FUERA DE ROTACION"

        print(f"TITULO: {cancion['titulo']}") 
        print(f"AÑO: {cancion['anio']}") 
        print(f"DURACION: {cancion['duracion']}")
        print(f"ESTADO {estado_texto}") 
        print("********************************") 

def main():
    lista_canciones = []

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == 1:
            agregar_cancion(lista_canciones)

        elif opcion == 2:
            print("BUSCAR CANCION")
            titulo = input("Ingrese el titulo de la cancion a buscar: ")
            posicion = buscar_cancion(lista_canciones, titulo)

            if posicion != -1:
                cancion = lista_canciones[posicion]
                print(f"Encontrada! Titulo: {cancion['titulo']} | Año: {cancion['anio']} | Duracion: {cancion['duracion']}  ")    
            else:
                print(f"La cancion '{titulo}' no se encuentra registrada.")

        elif opcion == 3:
            eliminar_cancion(lista_canciones)

        elif opcion == 4:
            actualizar_estados(lista_canciones)
            print("Estados de rotacion actualizados con exito segun el año")

        elif opcion == 5:
            mostrar_canciones(lista_canciones)

        elif opcion == 6:
            print("Gracias por usar el sistema de la radio, sigue escuchando")
            break

main()

        

        
               















    


                       
    


    

        
