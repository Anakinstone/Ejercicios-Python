cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:

    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


respuesta = 17
if respuesta != 42:
    print("Esta respuesta no es correcta")

usuarios_banadeos = ['pepe charly', 'jose', 'maria']

name= input('ingresa un nombre de usuario: ')

if name not in usuarios_banadeos:
    print(name.title() + " no esta baneado.")
else:
    print(name.title()) + " si esta baneado."

#Validar si es mayor de edad para votar
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Puedes votar")
else:
    print("Aun no puedes votar, disfruta tu libertad :v")

#Pase al evento
"""
if edad < 4:
    print("Tu entrada es gratuita")
elif edad <= 18:
    print("Tu entrada cuesta $50")
else:
    print("tu entrada cuesta $100")
"""

if edad < 4:
    precio = 0
elif edad < 18:
    precio = 50
else:
    precio = 100

print("La entrada te va a costar $" + str(precio))

print('''
Programa de operaciones aritmeticas teclee una operacion, ejem suma, resta, division, multiplicacion y dos numeros que desee evaluar
''')
operacion = input("Teclee la operacion: ")
num1 = int(input("Teclee el primer numero "))
num2 = int(input("Teclee el segundo numero "))

if operacion == "suma":
    resultado = num1 + num2
elif operacion == "resta":
    resultado = num1 - num2
elif operacion == "division":
    resultado = num1 / num2
elif operacion == "multiplicacion":
    resultado = num1 * num2
else:
    print("opcion no valida")

print("El resultado de la operacion " + str(operacion) + "es " + str(resultado))
#print("el resultado de la operacion {0} es {1}").format(operacion, resultado)
