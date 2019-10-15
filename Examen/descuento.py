descuento = int(input("Ingrese el porcentaje de descuento: "))
importe = int(input("ingrese el importe de producto: "))
def restar_descuento(desc, importe):
    diccionario = {"Descuento":desc,"importe":importe}
    porcentaje = importe * descuento / 100
    resultado = importe - porcentaje
    print("El costo a pagar es de: $", resultado)

restar_descuento(descuento, importe)