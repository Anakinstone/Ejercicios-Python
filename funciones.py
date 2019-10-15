#Funciones


def holaMundo():
    print("Hola Mundo")
holaMundo()

#parametros

def saludarUser(username='anakin'):
    print("Hola" + username)

saludarUser()

#Numeros condicionales
num1 = input("ingresa el primer numero:")
num2 = input("ingresa el segundo numero:")

def suma(num1=0, num2=0):
    total = num1 + num2
    print(total)

suma(num1, num2)

#Par e impar
num3 = int(input("Ingresa un numero mas: "))

def validar(num3):
    if(num3%2==0):
        print(str(num3)+" es par")
    else:
        print(str(num3)+" es impar")

validar(num3)

#Factorial
num4 = int(input("ingresa un numero para calcular su factorial: "))
def factorial(num4):

	fact_total = 1
	
	while num4 > 1:
		fact_total *= num4

		num4 -= 1


		print(num4, " > ", end="")

	print(" = ", fact_total)

factorial(num4)
#Crea una funcion que dados dos numeros mostrara todos los numeros entre ellos
num8 = int(input("Ingrese el primer rango de numero: "))
num9 = int(input("Ingrese el segundo rango de numero: "))

def rangos(num8, num9):

	for i in range(num8,num9):
		print(i)

rangos(num8, num9)