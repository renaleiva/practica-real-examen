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


    

        
