

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

def mostar_menu():
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

    titulo = validar_titulo
    anio = validar_anio
    duracion = validar_duracion

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

        












    


                       
    


    

        
