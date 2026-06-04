# UCamp_Project2
## ProjectA Longitud de una frase

### Este programa nos solicita ingresar una contraseña la cual tiene que tener entre 4 y 8 caracteres

* Encerramos el código en un while para que cuando se ingrese una contraseña incorrecta el programa nos haga repetir el proceso
* Así mismo usamos if elif para brindar mensajes al usuario dependiendo si le faltan o le sobran caracteres a su código

## ProjectB Encuentra el cuadrante

### Este programa nos indica ingresar uno o más puntos del tipo (x , y), y este nos indicará en qué cuadrante se encuentra este punto

* Primero solicitamos al usuario que ingrese el número de puntos que desea ingresar, así mismo lo guardamos en una variable que nos va a servir como contador para que se siga ejecutando el número de puntos que el usuario deseé, al igual con un while nos aseguramos que sean ingresados sólo números enteros
* Solicitamos ingresar las coordenadas las cuáles igual son verificadas con un while de que sean números enteros los ingresados
* Con funciones if elif devolvemos los datos de cada cuadrante
* Ingresamos también las dos situaciones donde los puntos se encuentren dentro del eje x y/o el eje y
* Por último la última situación posible que sería dentro del origen
* Ya para finalizar restamos 1 a nuestro contador para que se siga ejecutando hasta que sea igual a 0
