n = int(input("Dígame cuántas materias tiene: "))

if n < 1:
    print("Teclee por lo menos una materia:")
else:
    lista = []
    for i in range(n):
        print("Escriba el nombre de la materia", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("Las materias son:", lista)
