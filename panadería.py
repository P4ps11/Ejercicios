"""
Una panadería vende barras de pan a $3490 cada una. El pan que no es el día tiene un descuento del
 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
 Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le 
 hace por no ser fresca y el coste final total.
"""

barras = int(input("¿Cuantas barras deseas llevar?:  "))
precio_habitual = 3900
total_sin_descuento = barras * precio_habitual
total_descuento = (barras * precio_habitual) * 0.4

print("El costo total sin descuento sería de: $", total_sin_descuento , "pero como tiene un descuento del 60% le queda en: $", total_descuento)
