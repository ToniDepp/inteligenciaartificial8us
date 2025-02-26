import subprocess

def menu():
    print("Bienvenido al menu de los ejercicios realizados en clase por mi :) ")
    while True:
        print("\n-----Seleccione el ejercicio-----"
              "\nIngrese un numero del 1 al 26 (enteros)")
        opcion = input("Seleccione una opcion:\n")
        if opcion =="1":
            subprocess.run(["python", "E1CLASE.py"])

        elif opcion == "2":
            subprocess.run(["python", "E2CLASE.py"])
        
        elif opcion == "3":
            subprocess.run(["python", "E3CLASE.py"])

        elif opcion == "4":
            subprocess.run(["python", "E4CLASE.py"])

        elif opcion == "5":
            subprocess.run(["python", "E5CLASE.py"])

        elif opcion == "6":
            subprocess.run(["python", "E6CLASE.py"])

        elif opcion == "7":
            subprocess.run(["python", "E7CLASE.py"])

        elif opcion == "8":
            subprocess.run(["python", "E8CLASE.py"])

        elif opcion == "9":
            subprocess.run(["python", "E9CLASE.py"])

        elif opcion == "10":
            subprocess.run(["python", "E10CLASE.py"])

        elif opcion == "11":
            subprocess.run(["python", "E11CLASE.py"])

        elif opcion == "12":
            subprocess.run(["python", "E12CLASE.py"])

        elif opcion == "13":
            subprocess.run(["python", "E13CLASE.py"])

        elif opcion == "14":
            subprocess.run(["python", "E14CLASE.py"])

        elif opcion == "15":
            subprocess.run(["python", "E15CLASE.py"])

        elif opcion == "16":
            subprocess.run(["python", "E15MEJORA.py"])

        elif opcion == "17":
            subprocess.run(["python", "TEOREMA.py"])

        elif opcion == "18":
            subprocess.run(["python", "TEMPCITY.py"])

        elif opcion == "19":
            subprocess.run(["python", "TEMPERATURA.py"])

        elif opcion == "20":
            subprocess.run(["python", "NODOS.py"])

        elif opcion == "21":
            subprocess.run(["python", "17-U1.py"])

        elif opcion == "22":
            subprocess.run(["python", "18-E1.py"])

        elif opcion == "23":
            subprocess.run(["python", "181-1-E1.py"])

        elif opcion == "24":
            subprocess.run(["python", "181-2-E2.py"])

        elif opcion == "25":
            subprocess.run(["python", "182-2-E2.py"])

        elif opcion == "26":
            subprocess.run(["python", "183-1-E1.py"])

        else:
            print("Opcion no valida")

menu()