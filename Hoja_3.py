'''
Programa 1: en este programa, se le solicita al usuario ingresar una contraseña
 y posteriormente comprobarla.
'''

print("         Ejercicio 1    ")
print()

print("    Bienvenido al sistema   ")

password=str(input("Ingrese una contraseña: "))
cont_=0

for x in password:
    cont_+=1

if cont_ >=5:
    print("Contraseña segura")
else:
    print()
    print("Contraseña insegura")
    print()
    new_password=str(input("¿Desea ingresar una nueva contraseña? (Ingrese si o no): "))
    if new_password == "si":
        print()
        print("*Sugerencia: Ingrese una contraseña de mas de 5 caracteres")
        password=str(input("Ingrese una contraseña nueva: "))

print()
password_confirm=str(input("Ingrese la contraseña seleccionada: "))

while password_confirm != password:
    print("La contraseña no es correcta")
    password_confirm=str(input("Ingrese la contraseña nuevamente: "))

print()
print("Contraseña correcta, bienvenido.")
print()
print("----------------------")

'''
Programa 2: en este programa, se le solicita al usuario ingresar su nombre y su sexo
para clasificarlo en un grupo A (mujeres con nombre anterior a la M y hombres con nombre posterior a la N)
y el grupo B que es el resto.
'''
print("    Ejercicio 2   ")
print()

nombre=str(input("Ingrese su nombre: "))
sexo=str(input("Ingrese su sexo (hombre o mujer): "))

if sexo == "mujer":
    if nombre.lower() < "M":
        grupo="A"
    else:
        grupo="B"
else:
    if nombre.lower() > "N":
         grupo="A"
    else:
        grupo="B"
print()
print("El grupo al que pertenece es el: "+ grupo)
