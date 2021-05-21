'''
    Hoja de trabajo 1 del curso de python básico:
La función del siguiente código es realizar el cálculo del índice de masa corporal.
'''

print()
print("Hola, bienvenido a la calculadora de IMC")
print()
peso=float(input("Ingrese su peso en kg: "))            #Definición de la variable peso
estatura=float(input("ingrese su estatura en m: "))     #Definición de la variable estatura
print()
IMC=float(round(peso/estatura**2,2))                    #Cálculo del IMC, peso/estatura ** 2
print("Su IMC es", IMC, "kg/m**2")
print()

print("Salud")
if IMC <= 18.5:
    print("Sufre delgadez")
if IMC > 18.5 and IMC < 24.9:
    print("Usted es saludable")
if IMC >= 24.9:
    print("Deje de comer Mcdonalds")
print()