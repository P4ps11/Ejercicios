# Programa para ver estado de peso
peso = float(input("¿Cuanto pesas en kg?:  "))
altura = float(input("¿Cuanto mides en metros?:  "))
imc = round((peso) / (altura) ** 2)
print("tu índice de masa corporal es de", imc)

if imc < 18.5:
    print("Tu peso es muy bajo, come más")
elif imc < 25:
    print("Tu peso esta normal, felicitaciones!")
elif imc < 30:
    print("Estas en sobrepeso, haz más ejercicio")
else:
    print("¡Estas obeso!, come menos y haz")
