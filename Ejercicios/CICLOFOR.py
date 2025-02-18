def es_primo(n, m):
    if n < 2:
        return False
    else:
        for i in range(2, m + 1):
            if n % 2 == 0:
                return True
            return False

inicio = int(input("Ingrese un valor de inicio:\n"))
final = int(input("Ingrese un valor de inicio:\n"))

print(f"Numeros pares entre {inicio} y {final}")
for num in range(inicio,final +1):
    if es_primo(num, final):
        print(num, " ")