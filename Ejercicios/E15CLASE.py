
nombre = input("Ingrese su Nombre: ");
producto = input("Ingrese el nombre del producto: ")
total_compra = float(input("Ingrese el total de tu compra: "));
if total_compra > 100:
    descuento = total_compra * 0.10;
    total_final = total_compra - descuento;
    print(f"¡Felicidades{nombre}! tienes un descuento del 10% por la compra del producto {producto}. El total aa pagar es: {total_final}");
else:
    print(f"El total a pagar es: {total_compra}");
