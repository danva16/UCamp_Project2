#encerramos el código en un bucle while para que el usuario pueda intentar ingresar una contraseña válida hasta que lo logre
while True:
    #Se le solicita al usuario que ingrese una contraseña y se le indicará si la contraseña es válida o no.
    #La contraseña debe tener entre 4 y 8 caracteres
    contraseña_usuario = input("Ingrese una contraseña (entre 4 y 8 caracteres): ")
    lengthpassword = len(contraseña_usuario)
    #se crea la función si la contraseña es correcta
    if 4 <= lengthpassword <= 8:
        print(f"La contraseña {contraseña_usuario} fue guardada correctamente")
        break
    #se muestra un mensaje si la contraseña contiene menos caracteres de los solicitados
    elif lengthpassword < 4:
        #se muestra un mensaje si la contraseña contiene un caracter
        if lengthpassword == 1:
            print(f"La contraseña es demasiado corta. Solo tiene {lengthpassword} caracter.\n")
            print("Favor de intentarlo de nuevo.")
        else:
            print(f"La contraseña es demasiado corta. Solo tiene {lengthpassword} caracteres.\n")
            print("Favor de intentarlo de nuevo.")
    #se muestra un mensaje si la contraseña contiene más caracteres de los solicitados
    elif lengthpassword > 8:
        print(f"La contraseña es demasiado larga. Tiene {lengthpassword} caracteres.\n")
        print("Favor de intentarlo de nuevo.")