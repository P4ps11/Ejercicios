"""Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular 
y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear 
cada cantidad a dos decimales.
"""
total_inicial = float(input("¿Cuanto dinero vas a introducir a la cuenta de ahorros?:  "))
intereses_primer_año = total_inicial * 0.04
total_primer_año = intereses_primer_año + total_inicial
intereses_segundo_año = total_primer_año * 0.04
total_segundo_año = intereses_segundo_año + total_primer_año
intereses_tercer_año = total_segundo_año * 0.04
total_tercer_año = intereses_tercer_año + total_segundo_año
print("Su capital total en un año será de: $", total_primer_año)
print("Su capital total en dos años será de: $", total_segundo_año)
print("Su capital total en tres años será de: $", total_tercer_año)
