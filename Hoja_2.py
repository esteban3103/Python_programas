'''
Programa 1: 
    Este programa solicita al usuario un número entero y realice
    un triángulo rectángulo.
'''
print()
print("    Ejercicio 1     ")
num_1=int(input("Ingrese un número entero positivo: "))   #El programa solicita al usuario un número
for x in range(1,num_1+1):                               #Estructura cíclica que permitirá acumular el *       
    cont=0                                               #variable usada como contador
    while cont<x:                                           
        print("*", end='')                               #impresión que elimina el salto de línea
        cont+=1
    print()  
print()

print("----------------------------------")
'''
Programa 2
    Este programa solicita al usuario un número entero positivo y realiza
    el conteo descendente hasta 0. 
'''
print("    Ejercicio 2    ")

num_2=int(input("Ingrese un número entero positivo: "))    #Solicita al usuario ingresar un número.

for x in range(0,num_2+1):                                 #Estructura que permite incrementar el valor de x
    print(num_2-x, end='')                                 #Reste del número a ingresar
    if(num_2-x==0):                                        #condición que permite salir del ciclo.
        break
    print(", ", end='')
print(".")    

print()
print("----------------------------")
'''
    Programa 3
Este programa solicita al usuario un número entero y determina si el número es primo o no lo es.
'''    

print("    Ejercicio 3    ")

num_3=int(input("Ingrese un número entero positivo: "))

x=2
while num_3%x !=0:
    x+=1
if x==num_3:
    print(str(num_3)+" es un número primo.")
else:
    print(str(num_3)+" no es un número primo.")