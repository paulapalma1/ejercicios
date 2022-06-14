import numpy as np

llenarasientos=1
asientos=np.zeros((7,6), dtype=int)

for f in range(7):
    for c in range(6):
        asientos[f][c]=int(llenarasientos)
        llenarasientos=llenarasientos+1

print(asientos)

def agregar_cero_si_es_necesario(valor):
    return f"{valor:02d}"

def asientosdisponibles():
    for f in range(7):
        print("\n")
        if f==5:
            print("-"*20)
        for c in range(6):
            if asientos[f][c]!=0:
                print(agregar_cero_si_es_necesario (asientos[f][c]), end=" ") 
            else:
                print("X ", end=" ")

def comprarasiento(asientos,numasiento):
    for f in range(7):
        for c in range(6):
            if asientos[f][c]==0:
                print("asiento no disponible")               
            if asientos[f][c]==numasiento:
                asientos[f][c]=0
    return (asientos)

def solicitarnombre(nombre,numasiento):
    nombre[numasiento]=input("Ingrese el nombre del pasajero: ")
    return(nombre)

#repetir para los demás datos

def solicitardatos(numasiento, nombre, rut, telefono, banco):
    n=numasiento
    nombre[n]=input("Ingrese el nombre del pasajero: ")
    rut[n]=input("Ingrese el rut del pasajero: ")
    telefono[n]=input("Ingrese el teléfono del pasajero: ")
    banco[n]=input("Ingrese el banco del pasajero: ")
    if banco.lower()=="duoc":
        descuento=0.15
    return(nombre,rut,telefono,banco,descuento)
    
        




op=6
while op!=5:
    print("\n\n***MENU***")
    print("*"*10)
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos pasajero")
    print("5. Salir")
    print("*"*10)
    op=int(input("Ingrese una opción: " ))
    
    if op==1:
        asientosdisponibles()

    if op==2:
        numasiento=int(input("Ingrese el número de asiento que desea comprar: "))
        if numasiento>0 and numasiento<43:
            asientos=comprarasiento(asientos,numasiento)
            if numasiento<31:
                print("Su asiento es normal")
                print("El precio de su asiento es: $78.900")
            else:
                print("su asiento es VIP")
                print("el precio de su asiento es: $240.000")
            confirma=input("¿Desea continuar con la compra? (si/no): ")
            confirma.lower()
            if confirma=="si":
                asientos=comprarasiento(asientos,numasiento)
                (nombre,rut,telefono,banco)=solicitardatos(numasiento, nombre, rut, telefono, banco)
        else:
            print("El número de asiento debe estar ser entre 1 y 42")
        