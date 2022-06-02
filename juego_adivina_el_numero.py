# Este es un juego de adivina el numero

import random

#Imprime el mensaje de bienvenida del juego

print('Bienvenido al juego de "Adivina el numero en 3 intentos"')

#Define el numero ganador y solicita un numero de suerte al usuario
numeroGanador = random.randint(1,10) #Genera un numero aleatorio entre 1 y 10.
numeroIngresado = int(input('Ingresa tu numero de la suerte entre 1 y 10: ')) #Solicita un numero entre 1 y 10.
numeroDeVeces = 1 #Pone el numero de intentos en 1.

#Compara el numero de entrada con el ganador para indicar si el numero ingresado es igual al numero 
#ganador o el ganador esta mas arriba o mas abajo, siempre que haya menos de 3 intentos.    

while numeroGanador != numeroIngresado: #Si el numero ingresado es diferente al ganador, entra a este while.
    if numeroDeVeces <3:    # Si el numero de intentos < 3, sigue estas secuencia.
        numeroDeVeces += 1  # Incrementa en 1 el numero de intentos por cada ciclo while.
        if numeroGanador > numeroIngresado: #Si el num ganador > al ingresado, solicita un nuevo ingreso y vuelve al while.
            numeroIngresado = int(input(f'El numero ganador esta mas arriba. Ingresa otro numero de la suerte: '))
        elif numeroGanador < numeroIngresado: #Si el num ganador < al ingresado, solicita un nuevo ingreso y vuelve al while
            numeroIngresado = int(input(f'El numero ganador esta mas abajo. Ingresa otro numero de la suerte: '))
    else: # Si num intentos = 3, print esto, reinicia el num de intentos, genera un nuevo num ganador y vuelve al while.
        print(f'Rayos! lo intentaste {numeroDeVeces} veces y no lo lograste. Para la proxima sera!')
        numeroIngresado = int(input('Intentalo de nuevo, Ingresa tu numero de la suerte'))
        numeroGanador = random.randint(1,10) #genera el nuevo num ganador.
        numeroDeVeces = 1    #reinicia el numero de intentos.
#Si el numero ingresado es igual al ganador entonces..

if numeroDeVeces == 1:
    print(f'Felicidades! {numeroGanador} es el numero correcto. Te acabas de ganar un Wisky 18 anios. Ganaste al primer intento, que muvi!')            
elif numeroDeVeces == 3:
    print(f'Felicidades! {numeroGanador} es el numero correcto. Te acabas de ganar un Helado. Ganaste en el ultimo intento!')
else:
    print(f'Felicidades! {numeroGanador} es el numero correcto. Te acabas de ganar un like en tus redes. Ganaste en {numeroDeVeces} intentos, que muvi!')        
            

    








    
    
    
