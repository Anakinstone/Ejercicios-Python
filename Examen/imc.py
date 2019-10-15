print("Indice de masa corporal")
masa = float(input("ingresa tu peso en Kilogramos: "))
altura = float(input("ingresa tu altura en metros: "))
imc = masa / (altura*altura)

if imc < 15:
    estado = "Delgadez muy severa"
elif imc >= 15:
    estado = "Delgadez severa"
elif imc >= 16:
    estado = "Delgadez"
elif imc >= 18.5:
    estado = "Peso saludable"
elif imc >= 25:
    estado = "Sobre peso"
elif imc >= 30:
    estado = "Obesidad moderada"
elif imc >= 35:
    estado = "Obesidad severa"
else:
    estado = "obesidad morbida"

print("Tu índice de masa corporal es "+ str(imc) + "y tienes " + estado)