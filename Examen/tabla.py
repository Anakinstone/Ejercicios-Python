numero = int(input("Introduce un numero para optener su tabla: "))
def imprimir_tabla(numero):
    # Se supone que las tablas llegan hasta el 10
    LIMITE = 10
    # Comenzar en 1
    contador = 1
    while contador <= LIMITE:
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
        # Incrementar contador para no caer en ciclo infinito
        contador = contador + 1

imprimir_tabla(numero)