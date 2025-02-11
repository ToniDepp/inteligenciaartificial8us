#Pedir el primer numero
numero1 = float(input("Introduce el primer numero:\n"));

#Pedir el segundo numero
numero2 = float(input("Introduce el segundo numero:\n"));

#Realiza una operacion simple (resta y multiplicacion)
resta = numero1 - numero2
mul = numero1 * numero2

#Mostrar el resultado con salto de linea
print(f"\nLa resta de {numero1} y {numero2} es: {resta}\n"
      f"La multiplicacion de {numero1} y {numero2} es: {mul}")