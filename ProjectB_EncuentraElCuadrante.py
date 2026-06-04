#Código que solicita al usuario ingresar las coordenadas de un punto en el plano cartesiano y determina en qué cuadrante se encuentra ese punto.
while True:
    #solicitamos al usuario que ingrese el número de puntos que desea ingresar
    try:
        numero_de_puntos = int(input("Ingrese el número de puntos que desea ingresar: "))
        break
    except ValueError:
        print("Por favor, ingrese un número entero.")

while numero_de_puntos > 0:
    while True:
        #solicitamos al usuario que ingrese las coordenadas del punto
        try:
            x = int(input("Ingrese la coordenada x del punto: "))
            y = int(input("Ingrese la coordenada y del punto: "))
            break
        except ValueError:
            print("Por favor, ingrese coordenadas válidas(números enteros).")

    #verificamos que el punto esté dentro del primer y cuarto cuadrante
    if x > 0:
        if y > 0:
            print(f"El punto {(x, y)} se encuentra en el primer cuadrante.")
        elif y < 0:
            print(f"El punto {(x, y)} se encuentra en el cuarto cuadrante.")
    #verificamos que el punto esté dentro del segundo y tercer cuadrante
    elif x < 0:
        if y > 0:
            print(f"El punto {(x, y)} se encuentra en el segundo cuadrante.")
        elif y < 0:
            print(f"El punto {(x, y)} se encuentra en el tercer cuadrante.")
    elif x == 0 and y != 0:
        print(f"El punto {(x, y)} se encuentra sobre el eje y.")
    elif y == 0 and x != 0:
        print(f"El punto {(x, y)} se encuentra sobre el eje x.")
    else:
        print("El punto (0, 0) se encuentra en el origen.")
    
    #restamos 1 al número de puntos para que el ciclo se ejecute hasta que se hayan ingresado todos los puntos
    numero_de_puntos -= 1