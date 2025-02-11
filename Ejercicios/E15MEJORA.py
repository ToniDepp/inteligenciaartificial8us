import datetime;
import random;

fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
folio = random.randint(1000,9999);

nombre = input("Ingrese su Nombre: ");
producto = input("Ingrese el nombre del producto: ")
total_compra = float(input("Ingrese el total de tu compra: "));
if total_compra > 100:
    descuento = total_compra * 0.10;
    total_final = total_compra - descuento;
    print(f"----------- TICKET DE COMPRA -----------\n"
          "Tienda: OXXO\n"
          f"Folio: {folio}\n"
          f"Fecha y Hora: {fecha}\n"
          "---------------------------------------\n"
          f"Cliente: {nombre}\n"
          f"Producto: {producto}\n"
          f"Total de la compra: {total_compra}\n"
          f"Descuento: {descuento}\n"
          f"Total a pagar: {total_final}\n"
          "---------------------------------------\n"
          "¡Gracias por su Compra! ¡Vuelva pronto!");
else:
    print(f"El total a pagar es: {total_compra}");