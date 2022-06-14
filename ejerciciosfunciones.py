def calculariva(precio):
    iva=precio*0.19
    return iva

def calculodescuento(precio,descuento):
    descuento=precio*descuento/100
    return descuento

def calculoimc(peso,estatura):
    IMC=peso/(estatura**2)
    return IMC

op=3
while op!=4:
    print("***MENU***")
    print("*"*10)
    print("1. Calcular IVA")
    print("1. Descuento")
    print("1. Calcular IMC")
    print("4. SALIR")
    op=int(input("Ingrese su opción: (1:4):"))
    if op==1:
        precio=int(input("Ingrese precio del producto: ")) 
        iva=int(calculariva(precio))
        print("El IVA del producto es: ", iva)
    
    if op==2:
        precio=int(input("Ingrese precio del producto: ")) 
        descuento=int(input("Ingrese el porcentaje de descuento: "))
        valordesc=int(calculodescuento(precio,descuento))
        print("El monto de descuento es: ", valordesc) 
        valorfinal=int(precio-valordesc)
        print("El precio con el descuento aplicado es: ", valorfinal)

    if op==3:
        peso=float(input("Ingrese el peso: "))
        estatura=float(input("Ingrese la estatura: "))
        IMC=calculoimc(peso,estatura)
        print("Su IMC es: ", round(IMC,2))
        if IMC<18.5:
            print("Bajo peso")
        elif IMC<24.9:
            print("peso adecuado")
        elif IMC<29.9:
            print("sobrepeso")
        elif IMC<34.9:
            print("obesidad grado 1")
        elif IMC<39.9:
            print("obesidad grado 2")
        else:
            print("obesidad grado 3")