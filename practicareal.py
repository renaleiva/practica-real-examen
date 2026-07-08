def validar_titulo():
    while True:
        titulo = input("Ingrese el titulo de la cancion: ")
        if titulo.strip() == "":
            print("Error: El titulo no puede estar vacio ni contener espacios.")
        else:
            return titulo
        
        