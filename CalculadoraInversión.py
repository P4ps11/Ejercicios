"""
Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital 
obtenido en la inversión.
"""
cantidad = float(input("¿Cuanto dinero va a invertir?:  "))
interes_anual = float(input("¿A que interes anual (%) invertirá?:  "))
años = float(input("¿A cuantos años hara su inversión?:  "))
print("Al final de la inversión tendra una canitad total de $" , int(((cantidad) + (cantidad) * (interes_anual * 0.01) * (años))))
